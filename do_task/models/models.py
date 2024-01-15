# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ToDo(models.Model):
    _name = "dodev.todo"
    _description = "The DO Dev To Do Odoo Module"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description", required=False)
    state = fields.Selection(
        [
            ("pending", "Pending"),
            ("in_progress", "In Progress"),
            ("done", "Done"),
        ],
        string="State",
        default="pending",
    )
