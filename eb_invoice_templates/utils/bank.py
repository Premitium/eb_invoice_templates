# eb_invoice_templates/utils/bank.py
from __future__ import annotations
import frappe
from typing import Optional, Dict, Any

def _first(x): return x[0] if x else None
def _pick(obj, *keys):
    get = (obj.get if isinstance(obj, dict) else lambda k: getattr(obj, k, None))
    for k in keys:
        v = get(k)
        if v not in (None, ""):
            return v
    return None

def resolve_bank_account_name(doc) -> Optional[str]:
    # 1) chosen on the invoice
    ba = getattr(doc, "company_bank_account", None) or getattr(doc, "bank_account", None)
    if ba: return ba
    # 2) receivable / payable account default bank
    acc_name = getattr(doc, "debit_to", None) or getattr(doc, "credit_to", None)
    if acc_name:
        acc = frappe.get_cached_doc("Account", acc_name)
        if getattr(acc, "default_bank_account", None):
            return acc.default_bank_account
    # 3) company default
    dflt = frappe.get_all("Bank Account",
        filters={"company": doc.company, "is_company_account": 1, "is_default": 1},
        pluck="name", limit=1)
    if dflt: return dflt[0]
    # 4) any company bank account
    any_ba = frappe.get_all("Bank Account",
        filters={"company": doc.company, "is_company_account": 1},
        pluck="name", limit=1)
    return _first(any_ba)

def _find_bank_from_text(bank_name_text: str) -> Optional[str]:
    """If BA only has bank_name (text), try to find a Bank record."""
    if not bank_name_text:
        return None
    by_label = frappe.get_all("Bank", filters={"bank_name": bank_name_text}, pluck="name", limit=1)
    if by_label: return by_label[0]
    by_name  = frappe.get_all("Bank", filters={"name": bank_name_text}, pluck="name", limit=1)
    return _first(by_name)

def get_bank_account_details(ba_name: str, company_fallback: Optional[str] = None) -> Dict[str, Any]:
    """
    Return a normalized dict for printing.
    Keys: name, holder, bank_name, account_no, iban, swift, bank_address
    """
    ba = frappe.get_cached_doc("Bank Account", ba_name)

    # Resolve linked Bank (or guess from text bank_name)
    bank_doc = None
    bank_link = _pick(ba, "bank")  # Link → Bank
    if bank_link:
        bank_doc = frappe.get_cached_doc("Bank", bank_link)
    else:
        bank_text = _pick(ba, "bank_name")
        bank_id = _find_bank_from_text(bank_text)
        if bank_id:
            bank_doc = frappe.get_cached_doc("Bank", bank_id)

    holder = _pick(ba, "account_name", "account_holder_name") or company_fallback
    bank_name = _pick(bank_doc or {}, "bank_name", "name") or _pick(ba, "bank_name", "bank")
    account_no = _pick(ba, "bank_account_no", "account_no")
    iban = _pick(ba, "iban")

    # >>> SWIFT fix: prefer Bank.swift_number, then other variants; fallback to BA if present
    swift = (
        (bank_doc and _pick(bank_doc, "swift_number", "swift_code", "swift", "bic"))
        or _pick(ba, "swift_number", "swift_code", "swift", "bic")
    )

    bank_address = _pick(ba, "bank_address")

    return {
        "name": ba.name,
        "holder": holder,
        "bank_name": bank_name,
        "account_no": account_no,
        "iban": iban,
        "swift": swift,
        "bank_address": bank_address,
    }

def eb_bank_block(doc) -> str:
    ba_name = resolve_bank_account_name(doc)
    if not ba_name:
        return ""
    d = get_bank_account_details(ba_name, company_fallback=getattr(doc, "company", None))
    esc = frappe.utils.escape_html
    parts = ['<div class="bank-block" style="margin-top:10px;">', "<strong>Bank Details</strong><br>"]
    if d.get("holder"):     parts.append(f"Beneficiary: {esc(d['holder'])}<br>")
    if d.get("bank_name"):  parts.append(f"Bank: {esc(d['bank_name'])}<br>")
    if d.get("account_no"): parts.append(f"Account No.: {esc(d['account_no'])}<br>")
    if d.get("iban"):       parts.append(f"IBAN: {esc(d['iban'])}<br>")
    if d.get("swift"):      parts.append(f"SWIFT/BIC: {esc(d['swift'])}<br>")
    if d.get("bank_address"):
        parts.append(esc(d["bank_address"]).replace("\n", "<br>"))
    parts.append("</div>")
    return "".join(parts)

def eb_bank_details(doc) -> Dict[str, Any]:
    ba_name = resolve_bank_account_name(doc)
    return get_bank_account_details(ba_name, company_fallback=getattr(doc, "company", None)) if ba_name else {}
