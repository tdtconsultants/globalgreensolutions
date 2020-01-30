# -*- coding: utf-8 -*-
from odoo import http

# class TdtMosCustomer(http.Controller):
#     @http.route('/tdt_mos_customer/tdt_mos_customer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tdt_mos_customer/tdt_mos_customer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tdt_mos_customer.listing', {
#             'root': '/tdt_mos_customer/tdt_mos_customer',
#             'objects': http.request.env['tdt_mos_customer.tdt_mos_customer'].search([]),
#         })

#     @http.route('/tdt_mos_customer/tdt_mos_customer/objects/<model("tdt_mos_customer.tdt_mos_customer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tdt_mos_customer.object', {
#             'object': obj
#         })