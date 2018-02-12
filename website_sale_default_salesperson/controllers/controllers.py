# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteSaleDefaultSalesperson(http.Controller):
#     @http.route('/website_sale_default_salesperson/website_sale_default_salesperson/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_sale_default_salesperson/website_sale_default_salesperson/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_sale_default_salesperson.listing', {
#             'root': '/website_sale_default_salesperson/website_sale_default_salesperson',
#             'objects': http.request.env['website_sale_default_salesperson.website_sale_default_salesperson'].search([]),
#         })

#     @http.route('/website_sale_default_salesperson/website_sale_default_salesperson/objects/<model("website_sale_default_salesperson.website_sale_default_salesperson"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_sale_default_salesperson.object', {
#             'object': obj
#         })