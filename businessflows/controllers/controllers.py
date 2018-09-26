# -*- coding: utf-8 -*-
from odoo import http

# class Businessflows(http.Controller):
#     @http.route('/businessflows/businessflows/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/businessflows/businessflows/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('businessflows.listing', {
#             'root': '/businessflows/businessflows',
#             'objects': http.request.env['businessflows.businessflows'].search([]),
#         })

#     @http.route('/businessflows/businessflows/objects/<model("businessflows.businessflows"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('businessflows.object', {
#             'object': obj
#         })