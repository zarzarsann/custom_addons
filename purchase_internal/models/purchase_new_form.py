from odoo import models, fields

class MyModel(models.Model):
    _name = 'purchase.new'
    _description = 'Purchase New'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(default=True)





