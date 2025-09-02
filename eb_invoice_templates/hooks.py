app_name = "eb_invoice_templates"
app_title = "ExiceBro Invoice Templates"
app_publisher = "Simeon Parvanov"
app_description = "Creates localized invoice templates for ErpNext"
app_email = "simo@sofiaelectricbrewing.com"
app_license = "gpl-3.0"

# erp_invoice_templates/erp_invoice_templates/hooks.py
fixtures = [
    {"dt": "Print Format", "filters": [["name", "in", [
        "Sales Invoice - My Custom",
        # add more print formats here
    ]]]},
    {"dt": "Property Setter", "filters": [["name", "in", [
        # e.g. Default Print Format for Sales Invoice
        "Sales Invoice-default_print_format"
    ]]]},
    {"dt": "Custom Field", "filters": [["name", "in", [
        # list any Custom Fields used in your template (if any)
        # e.g. "Sales Invoice-your_custom_field"
    ]]]},
    # optionally ship a specific Letterhead if it's unique to this template:
    # {"dt": "Letterhead", "filters": [["name", "in", ["My Company Letterhead"]]]},
]

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "eb_invoice_templates",
# 		"logo": "/assets/eb_invoice_templates/logo.png",
# 		"title": "ExiceBro Invoice Templates",
# 		"route": "/eb_invoice_templates",
# 		"has_permission": "eb_invoice_templates.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/eb_invoice_templates/css/eb_invoice_templates.css"
# app_include_js = "/assets/eb_invoice_templates/js/eb_invoice_templates.js"

# include js, css files in header of web template
# web_include_css = "/assets/eb_invoice_templates/css/eb_invoice_templates.css"
# web_include_js = "/assets/eb_invoice_templates/js/eb_invoice_templates.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "eb_invoice_templates/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "eb_invoice_templates/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "eb_invoice_templates.utils.jinja_methods",
# 	"filters": "eb_invoice_templates.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "eb_invoice_templates.install.before_install"
# after_install = "eb_invoice_templates.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "eb_invoice_templates.uninstall.before_uninstall"
# after_uninstall = "eb_invoice_templates.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "eb_invoice_templates.utils.before_app_install"
# after_app_install = "eb_invoice_templates.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "eb_invoice_templates.utils.before_app_uninstall"
# after_app_uninstall = "eb_invoice_templates.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "eb_invoice_templates.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"eb_invoice_templates.tasks.all"
# 	],
# 	"daily": [
# 		"eb_invoice_templates.tasks.daily"
# 	],
# 	"hourly": [
# 		"eb_invoice_templates.tasks.hourly"
# 	],
# 	"weekly": [
# 		"eb_invoice_templates.tasks.weekly"
# 	],
# 	"monthly": [
# 		"eb_invoice_templates.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "eb_invoice_templates.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "eb_invoice_templates.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "eb_invoice_templates.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["eb_invoice_templates.utils.before_request"]
# after_request = ["eb_invoice_templates.utils.after_request"]

# Job Events
# ----------
# before_job = ["eb_invoice_templates.utils.before_job"]
# after_job = ["eb_invoice_templates.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"eb_invoice_templates.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

