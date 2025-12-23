from odoo import _, api, exceptions, fields, models
from datetime import date

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    # @api.onchange('partner_id')
    # def _onchange_partner_id(self):
    #     if self.partner_id:
    #         partner_id = self.partner_id.id
    #         vendor_code = self.env['res.partner'].browse(partner_id).vendor_code
    #         if vendor_code:
    #             self.partner_ref = vendor_code
    #         else:
    #             self.partner_ref = ''
