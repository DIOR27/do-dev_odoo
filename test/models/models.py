# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class StageUcuencaTest(models.Model):
    _name = "ucuenca.test.stage"
    _description = "Etapa de prueba para la Universidad de Cuenca"

    name = fields.Char(
        string="Nombre",
        required=True,
        help="Nombre de la etapa",
    )
    sequence = fields.Integer(string="Secuencia", default=0)


class test(models.Model):
    _name = "ucuenca.test"
    _description = "Módulo de prueba para la Universidad de Cuenca"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Secuencia",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _("Nuevo"),
    )
    value = fields.Integer(
        string="Valor",
        help="Este es el valor de la prueba",
    )
    description = fields.Text()
    stage_id = fields.Many2one("ucuenca.test.stage", string="Etapa", default=1)

    test_line_ids = fields.One2many(
        "ucuenca.test.line", "test_id", string="Líneas de prueba"
    )

    """
    Override the create method to set a default value for the 'name' field if it is not provided.

    :param vals: A dictionary containing the field values for the new record.
    :return: The created record.
    """

    @api.model
    def create(self, vals):
        if vals.get("name", _("Nuevo")) == _("Nuevo"):
            vals["name"] = self.env["ir.sequence"].next_by_code("ucuenca.test") or _(
                "Nuevo"
            )
        return super(test, self).create(vals)

    """
    La función `test_sample` devuelve un diccionario que contiene información para mostrar un
    mensaje de notificación de éxito.
    """

    def test_sample(self):
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "message": "hola",
                "type": "success",
                "sticky": False,
            },
        }

    """
    La función `next_stage` actualiza la etapa de una entidad de prueba en función de su etapa
    actual, con manejo de errores para etapas no válidas o finales.
    """

    def next_stage(self):

        current_stage = self.stage_id.name

        match self.stage_id.name:
            case "Pendiente":
                self.stage_id = (
                    self.env["ucuenca.test.stage"]
                    .search([("name", "=", "En Proceso")], limit=1)
                    .id
                )
            case "En Proceso":
                self.stage_id = (
                    self.env["ucuenca.test.stage"]
                    .search([("name", "=", "Finalizado")], limit=1)
                    .id
                )
            case "Finalizado":
                raise UserError("No se puede actualizar la etapa de un test finalizado")
            case _:
                raise UserError("La etapa del test no es válida")
        self.message_post(
            body="%s ha cambiado la etapa de %s a %s"
            % (self.env.user.name, current_stage, self.stage_id.name)
        )

    """
    La función `previous_stage` en Python actualiza la etapa de una prueba a la etapa anterior según
    la etapa actual, con manejo de errores para etapas no válidas.
    """

    def previous_stage(self):

        current_stage = self.stage_id.name

        match self.stage_id.name:
            case "Pendiente":
                raise UserError("No se puede actualizar la etapa de un test pendiente")
            case "En Proceso":
                self.stage_id = (
                    self.env["ucuenca.test.stage"]
                    .search([("name", "=", "Pendiente")], limit=1)
                    .id
                )
            case "Finalizado":
                self.stage_id = (
                    self.env["ucuenca.test.stage"]
                    .search([("name", "=", "En Proceso")], limit=1)
                    .id
                )
            case _:
                raise UserError("La etapa del test no es válida")
        self.message_post(
            body="%s ha cambiado la etapa de %s a %s"
            % (self.env.user.name, current_stage, self.stage_id.name)
        )

class TestLine(models.Model):
    _name = "ucuenca.test.line"
    _description = "Línea de prueba para la Universidad de Cuenca"

    test_name = fields.Char()
    test_value = fields.Integer()
    test_id = fields.Many2one("ucuenca.test", string="Test")
