# -*- coding: utf-8 -*-
from odoo import http

# class CalculateLocation(http.Controller):
#     @http.route('/calculate_location/calculate_location/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/calculate_location/calculate_location/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('calculate_location.listing', {
#             'root': '/calculate_location/calculate_location',
#             'objects': http.request.env['calculate_location.calculate_location'].search([]),
#         })

#     @http.route('/calculate_location/calculate_location/objects/<model("calculate_location.calculate_location"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('calculate_location.object', {
#             'object': obj
#         })