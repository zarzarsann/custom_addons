# License LGPL-3.0

{
    "name": "Odoo",
    "summary": "Odoo Custom",
    "version": "18.0.1.0.3",
    "category": "Website",
    "website": "https://github.com/OCA/web",
    "author": "LasLabs, Tecnativa, ITerra, Onestein, "
    "Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "installable": True,
    "depends": ["base","sale","report_xlsx"],
    "development_status": "Production/Stable",
    "data": ["views/sale_order_inherit_view.xml","report/new_sale_order_report_view.xml","report/new_sale_order_report_template.xml"],
    "sequence": 100,
}
