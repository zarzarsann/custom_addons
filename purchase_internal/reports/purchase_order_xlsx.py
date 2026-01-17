from odoo import models
import io
import xlsxwriter


def generate_xlsx_report(self, workbook, data, purchase_orders):
    sheet = workbook.add_worksheet('Purchase Order')
    bold = workbook.add_format({'bold': True})

    # Headers
    sheet.write(0, 0, 'Purchase Reference', bold)
    sheet.write(0, 1, 'Vendor Email', bold)

    row = 1
    for o in purchase_orders:
        sheet.write(row, 0, o.name)
        # Safe access to email via partner_id
        sheet.write(row, 1, o.partner_id.email or 'N/A')
        row += 1