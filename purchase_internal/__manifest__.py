# License LGPL-3.0

{
    "name": "Odoo",
    "summary": "Odoo Custom",
    "version": "18.0.1.0.3",
    "category": "Website",
    "website": "https://odoo.com",
    "license": "LGPL-3",
    "installable": True,
    "depends": ["base","purchase","purchase_stock"],
    "development_status": "Production/Stable",
    "data": [
            "data/ir_sequence.xml",
            "security/ir.model.access.csv",
             "views/purchase_new_form_view.xml",
             "views/purchase_order_inherit_view.xml",
             "views/purchase_sequence_views.xml",
             "views/purchase_report_templates.xml"],
    "sequence": 101,
}
