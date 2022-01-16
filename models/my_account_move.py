# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveLine(models.Model):
    """ Override AccountInvoice_line to add the link to the purchase order line it is related to"""
    _inherit = 'myaccount.move.line'

    purchase_line_id = fields.Many2one('am_purchase.order.line', 'Purchase Order Line', ondelete='set null', index=True)