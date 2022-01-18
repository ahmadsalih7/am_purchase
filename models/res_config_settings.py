# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    po_order_approval = fields.Boolean("Purchase Order Approval",
                                       default=lambda self: self.env.company.po_double_validation == 'two_step')
    po_double_validation = fields.Selection(related='company_id.po_double_validation', string="Levels of Approvals *",
                                            readonly=False)
    po_double_validation_amount = fields.Monetary(related='company_id.po_double_validation_amount',
                                                  string="Minimum Amount", currency_field='company_currency_id',
                                                  readonly=False)
    company_currency_id = fields.Many2one('res.currency', related='company_id.currency_id', string="Company Currency",
                                          readonly=True,
                                          help='Utility field to express amount currency')

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.po_double_validation = 'two_step' if self.po_order_approval else 'one_step'
