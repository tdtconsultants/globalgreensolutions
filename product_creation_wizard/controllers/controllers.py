# -*- coding: utf-8 -*-
from odoo import http

# class ProductCreationWizard(http.Controller):
#     @http.route('/product_creation_wizard/product_creation_wizard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_creation_wizard/product_creation_wizard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_creation_wizard.listing', {
#             'root': '/product_creation_wizard/product_creation_wizard',
#             'objects': http.request.env['product_creation_wizard.product_creation_wizard'].search([]),
#         })

#     @http.route('/product_creation_wizard/product_creation_wizard/objects/<model("product_creation_wizard.product_creation_wizard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_creation_wizard.object', {
#             'object': obj
#         })