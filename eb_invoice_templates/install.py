# eb_invoice_templates/install.py
import frappe

MODULE = "ExciseBro Invoice Templates"
APP = "eb_invoice_templates"
PRINT_NAME = "Sales Invoice - EB Template"
DT = "Sales Invoice"

HTML = '{% include "eb_invoice_templates/templates/includes/sales_invoice_v1.html" %}'

def _ensure_module():
    md = frappe.db.get_value("Module Def", MODULE, ["name", "app_name"], as_dict=True)
    if not md:
        frappe.get_doc({
            "doctype": "Module Def",
            "module_name": MODULE,
            "app_name": APP
        }).insert(ignore_permissions=True)
    else:
        if not md.app_name or md.app_name != APP:
            doc = frappe.get_doc("Module Def", MODULE)
            doc.app_name = APP
            doc.save(ignore_permissions=True)

def _ensure_print_format():
    if frappe.db.exists("Print Format", PRINT_NAME):
        pf = frappe.get_doc("Print Format", PRINT_NAME)
        changed = False
        if pf.doc_type != DT: pf.doc_type = DT; changed = True
        if getattr(pf, "print_format_type", None) != "Jinja":
            pf.print_format_type = "Jinja"; changed = True
        if getattr(pf, "custom_format", 1) != 1:
            pf.custom_format = 1; changed = True
        if getattr(pf, "disabled", 0):
            pf.disabled = 0; changed = True
        if getattr(pf, "module", MODULE) != MODULE:
            pf.module = MODULE; changed = True
        if pf.html != HTML:
            pf.html = HTML; changed = True
        if changed:
            pf.save(ignore_permissions=True)
        return

    frappe.get_doc({
        "doctype": "Print Format",
        "name": PRINT_NAME,
        "doc_type": DT,
        "module": MODULE,
        "print_format_type": "Jinja",
        "custom_format": 1,
        "disabled": 0,
        "html": HTML,
        "raw_printing": 0
    }).insert(ignore_permissions=True)

def _ensure_default_property_setter():
    # OPTIONAL: keep only if you want it as default in the dropdown
    ps_name = f"{DT}-default_print_format"
    if not frappe.db.exists("Property Setter", ps_name):
        frappe.get_doc({
            "doctype": "Property Setter",
            "doctype_or_field": "DocType",
            "doc_type": DT,
            "property": "default_print_format",
            "value": PRINT_NAME,
            "property_type": "Data",
            "name": ps_name
        }).insert(ignore_permissions=True)

def after_install():
    _ensure_module()
    _ensure_print_format()
    _ensure_default_property_setter()  # remove this if you don't want it as default

def ensure_print_format_default():
    after_install()
