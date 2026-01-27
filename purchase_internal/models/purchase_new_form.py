from odoo import models, fields, api
from odoo.fields import Boolean


class PurchaseNew(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'purchase.new'
    _description = 'Purchase New'

    name = fields.Char(string="Name", required=True, tracking=True, default='New', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('done', 'Confirm'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)
    partner_id = fields.Many2one(comodel_name='res.partner', required=True, tracking=True)
    user_id = fields.Many2one(comodel_name='res.users', required=True, tracking=True, default=lambda self: self.env.uid)
    description = fields.Text(string="Description")
    active = fields.Boolean(default=True)
    line_ids = fields.One2many('purchase.new.line','new_id', string='Lines')
    sent = fields.Boolean(default=False)

    def action_send_mail(self):
        template = self.env.ref(
            "purchase_internal.email_template_purchase_new_order",
            raise_if_not_found=False
        )
        if template:
            for order in self:
                template.send_mail(order.id, force_send=True)
                order.sent = True

    def action_approve(self):
        for record in self:
            record.state = 'approved'

    def action_cancel(self):
        for record in self:
            record.state = 'cancel'

    def action_confirm(self):
        for record in self:
            record.state = 'done'

    @api.model_create_multi
    def create(self, vals):
        for rec in vals:
            code = self.env['ir.sequence'].next_by_code('purchase.new')
            rec['name'] = code
        res = super().create(vals)
        return res

    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         if vals.get('name', 'New') == 'New':
    #             vals['name'] = self.env['ir.sequence'].next_by_code(
    #                 'purchase.new'
    #             ) or 'New'
    #
    #         purchase_vals = {
    #                 'partner_id': vals['partner_id'],
    #                 'partner_ref': vals['name']
    #                 }
    #         self.env['purchase.order'].create(purchase_vals)
    #     return super().create(vals_list)

class PurchaseNewLine(models.Model):
    _name = 'purchase.new.line'
    _description = 'Purchase New Line'

    new_id = fields.Many2one(
        'purchase.new',
        string='Purchase New',
        ondelete='cascade',
        required=True
    )

    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True
    )

    quantity = fields.Float(default=1.0)
    price_unit = fields.Float(string='Unit Price')

    subtotal = fields.Float(
        string='Subtotal',
        compute='_compute_subtotal',
        store=True
    )

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit

class PurchaseNewWizard(models.TransientModel):
    _name = 'purchase.new.wizard'
    _description = 'Purchase New Wizard'

    note = fields.Text(string="Note")
    confirm = fields.Boolean(string="Confirm")

    def action_confirm(self):
        active_id = self.env.context.get('active_id')
        if active_id:
            record = self.env['purchase.new'].browse(active_id)
            record.message_post(body=self.note or "Confirmed from wizard")








