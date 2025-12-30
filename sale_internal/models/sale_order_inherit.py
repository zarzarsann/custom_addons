# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
from odoo import api, fields, models
from random import choice
import string

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_email = fields.Char(string="Customer Email", store=True)
    customer_code = fields.Char(string="Customer Code")
    customer_phone = fields.Char(string="Customer Phone", default="123456")

    def generate(self, number_of_digits):
        cus_code = ''.join(choice(string.digits) for _ in range(number_of_digits))
        return cus_code

    @api.onchange('partner_id')
    def _onchange_partner_id_warning(self):
        if not self.partner_id:
            return

        partner = self.partner_id
        self.customer_email = partner.email
        cus_code = self.generate(4)
        self.customer_code = 'CUS_' + str(partner.id) + '_' + cus_code

        # If partner has no warning, check its company
        if partner.sale_warn == 'no-message' and partner.parent_id:
            partner = partner.parent_id

        if partner.sale_warn and partner.sale_warn != 'no-message':
            # Block if partner only has warning but parent company is blocked
            if partner.sale_warn != 'block' and partner.parent_id and partner.parent_id.sale_warn == 'block':
                partner = partner.parent_id

            if partner.sale_warn == 'block':
                self.partner_id = False

            return {
                'warning': {
                    'title': _("Warning for %s", partner.name),
                    'message': partner.sale_warn_msg,
                }
            }
