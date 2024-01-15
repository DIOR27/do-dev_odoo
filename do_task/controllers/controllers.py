# -*- coding: utf-8 -*-
# from odoo import http


# class DoTask(http.Controller):
#     @http.route('/do_task/do_task', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/do_task/do_task/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('do_task.listing', {
#             'root': '/do_task/do_task',
#             'objects': http.request.env['do_task.do_task'].search([]),
#         })

#     @http.route('/do_task/do_task/objects/<model("do_task.do_task"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('do_task.object', {
#             'object': obj
#         })

