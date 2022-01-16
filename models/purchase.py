# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _name = 'am_purchase.order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Purchase Order"
    _order = 'date_order desc, id desc'

    def _default_currency_id(self):
        company_id = self.env.context.get('force_company') or self.env.context.get('company_id') or self.env.company.id
        return self.env['res.company'].browse(company_id).currency_id

    name = fields.Char('Order Reference', required=True, copy=False, default='New')
    partner_ref = fields.Char('Vendor Reference', copy=False)
    date_order = fields.Datetime('Order Date', required=True, copy=False,
                                 default=fields.Datetime.now)
    date_approve = fields.Datetime('Confirmation Date', readonly=1, copy=False)
    user_id = fields.Many2one(
        'res.users', string='Purchase Representative',
        default=lambda self: self.env.user, check_company=True)
    company_id = fields.Many2one('res.company', 'Company', required=True, default=lambda self: self.env.company.id)
    currency_id = fields.Many2one('res.currency', 'Currency', required=True,
                                  default=_default_currency_id)
    partner_id = fields.Many2one('res.partner', string='Vendor', required=True,
                                 change_default=True,
                                 domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    state = fields.Selection([
        ('draft', 'RFQ'),
        ('sent', 'RFQ Sent'),
        ('to approve', 'To Approve'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')],
        string='Status', readonly=True, copy=False, default='draft', tracking=True)
    order_line = fields.One2many('am_purchase.order.line', 'order_id', string='Order Lines',
                                 states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True)
    notes = fields.Text('Terms and Conditions')
    amount_total = fields.Monetary(string='Total', store=True, readonly=True, currency_field='currency_id')


class PurchaseOrderLine(models.Model):
    _name = 'am_purchase.order.line'
    _description = 'Purchase Order Line'
    _order = 'order_id, sequence, id'

    def _default_currency_id(self):
        company_id = self.env.context.get('force_company') or self.env.context.get('company_id') or self.env.company.id
        return self.env['res.company'].browse(company_id).currency_id

    name = fields.Text(string='Description', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    product_qty = fields.Float(string='Quantity', digits='Product Unit of Measure', required=True)
    date_planned = fields.Datetime(string='Scheduled Date', index=True)
    company_id = fields.Many2one('res.company', related='order_id.company_id', string='Company', store=True,
                                 readonly=True)
    currency_id = fields.Many2one('res.currency', 'Currency', required=True,
                                  default=_default_currency_id)
    product_id = fields.Many2one('my_product.template', string='Product', domain=[('purchase_ok', '=', True)],
                                 change_default=True)
    product_type = fields.Selection(related='product_id.type', readonly=True)
    price_unit = fields.Float(string='Unit Price', required=True, digits='Product Price')

    price_subtotal = fields.Monetary(string='Subtotal', store=True, currency_field='currency_id')
    order_id = fields.Many2one('am_purchase.order', string='Order Reference', index=True, required=True,
                               ondelete='cascade')
    state = fields.Selection(related='order_id.state', store=True, readonly=False)
    invoice_lines = fields.One2many('myaccount.move.line', 'purchase_line_id', string="Bill Lines", readonly=True,
                                    copy=False)
