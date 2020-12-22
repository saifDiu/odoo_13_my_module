# -*- coding: utf-8 -*-
# from odoo import http


# class Custom/omUniversity(http.Controller):
#     @http.route('/custom/om_university/custom/om_university/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom/om_university/custom/om_university/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom/om_university.listing', {
#             'root': '/custom/om_university/custom/om_university',
#             'objects': http.request.env['custom/om_university.custom/om_university'].search([]),
#         })

#     @http.route('/custom/om_university/custom/om_university/objects/<model("custom/om_university.custom/om_university"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/om_university.object', {
#             'object': obj
#         })
