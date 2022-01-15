# -*- coding: utf-8 -*-
# from odoo import http


# class AmPurchase(http.Controller):
#     @http.route('/am_purchase/am_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/am_purchase/am_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('am_purchase.listing', {
#             'root': '/am_purchase/am_purchase',
#             'objects': http.request.env['am_purchase.am_purchase'].search([]),
#         })

#     @http.route('/am_purchase/am_purchase/objects/<model("am_purchase.am_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('am_purchase.object', {
#             'object': obj
#         })
