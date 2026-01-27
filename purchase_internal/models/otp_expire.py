from odoo import models, fields, api
from datetime import datetime, timedelta

class GenerateOTP(models.Model):
    _name = 'generate.otp'
    _inherit = 'mail.thread'
    _description = "Generate OTP"

    email = fields.Char(string='Email')
    phone_no = fields.Char(string="Phone No")
    otp_code = fields.Char(string='OTP Code')
    active = fields.Boolean(string='Active', default=True)

    def otp_expire(self):
        otps = self.env['generate.otp'].sudo().search([('active', '=', True)])
        if otps:
            for otp in otps:
                current_datetime = datetime.now()
                one_min = otp.create_date + timedelta(minutes=1)
                if current_datetime >= one_min:
                    otp_tbl = self.env['generate.otp'].sudo().search([('id', '=', otp.id)])
                    vals = otp_tbl.write({'active': False})
