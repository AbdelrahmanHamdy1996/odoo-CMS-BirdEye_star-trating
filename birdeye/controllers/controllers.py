# -*- coding: utf-8 -*-
# from odoo import http


# class Birdeye(http.Controller):
#     @http.route('/birdeye/birdeye/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/birdeye/birdeye/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('birdeye.listing', {
#             'root': '/birdeye/birdeye',
#             'objects': http.request.env['birdeye.birdeye'].search([]),
#         })

#     @http.route('/birdeye/birdeye/objects/<model("birdeye.birdeye"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('birdeye.object', {
#             'object': obj
#         })
