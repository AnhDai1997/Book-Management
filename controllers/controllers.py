# -*- coding: utf-8 -*-
# from odoo import http


# class QuanLySach(http.Controller):
#     @http.route('/quan_ly_sach/quan_ly_sach/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quan_ly_sach/quan_ly_sach/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('quan_ly_sach.listing', {
#             'root': '/quan_ly_sach/quan_ly_sach',
#             'objects': http.request.env['quan_ly_sach.quan_ly_sach'].search([]),
#         })

#     @http.route('/quan_ly_sach/quan_ly_sach/objects/<model("quan_ly_sach.quan_ly_sach"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quan_ly_sach.object', {
#             'object': obj
#         })
