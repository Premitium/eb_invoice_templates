# eb_invoice_templates/hooks.py
app_name = "eb_invoice_templates"
app_title = "ExciseBro Invoice Templates"
app_publisher = "Simeon Parvanov"
app_description = "Creates localized invoice templates for ERPNext"
app_email = "simo@sofiaelectricbrewing.com"
app_license = "gpl-3.0"

fixtures = [
    {"dt": "Print Format", "filters": [["name", "in", ["EB Sales Invoice v1"]]]},
    # If you want it as default (optional), include the Property Setter below
    # {"dt": "Property Setter", "filters": [["name", "in", ["Sales Invoice-default_print_format"]]]},
    {"dt": "Custom Field", "filters": [["name", "in", [
        "Sales Invoice Item-excise_code",
        "Sales Invoice Item-abv",
        "Sales Invoice Item-container",
        "Sales Invoice Item-ean",
        "Sales Invoice Item-country_of_origin",
    ]]]},
]

# add this near the top-level (or extend existing jinja config)
jinja = {
    "methods": [
        "eb_invoice_templates.utils.bank.eb_bank_block",
        "eb_invoice_templates.utils.bank.eb_bank_details",
        "eb_invoice_templates.utils.bank.resolve_bank_account_name",
    ]
}
# compatibility for older Frappe keys
jinja_methods = [
    "eb_invoice_templates.utils.bank.eb_bank_block",
    "eb_invoice_templates.utils.bank.eb_bank_details",
    "eb_invoice_templates.utils.bank.resolve_bank_account_name",
]


# safety net: ensure PF exists & default is set when installing/migrating
aafter_install = "eb_invoice_templates.install.after_install"
after_migrate = ["eb_invoice_templates.install.ensure_print_format_default"]