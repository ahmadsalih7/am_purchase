# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _name = 'am_purchase.order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Purchase Order"
    _order = 'date_order desc, id desc'

    name = fields.Char('Order Reference', required=True, copy=False, default='New')
    partner_ref = fields.Char('Vendor Reference', copy=False)
    date_order = fields.Datetime('Order Date', required=True, copy=False,
                                 default=fields.Datetime.now)
    date_approve = fields.Datetime('Confirmation Date', readonly=1, copy=False)
    user_id = fields.Many2one(
        'res.users', string='Purchase Representative',
        default=lambda self: self.env.user, check_company=True)
    company_id = fields.Many2one('res.company', 'Company', required=True, default=lambda self: self.env.company.id)
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
