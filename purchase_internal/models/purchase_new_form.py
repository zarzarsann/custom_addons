from odoo import models, fields

class MyModel(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'purchase.new'
    _description = 'Purchase New'

    name = fields.Char(string="Name", required=True, tracking=True)
    partner_id = fields.Many2one(comodel_name='res.partner', required=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(default=True)





