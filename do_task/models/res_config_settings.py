from odoo import _, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    value = fields.Integer(string="Valor", help="Este es el valor de la prueba")

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env["ir.config_parameter"].sudo().set_param(
            "ucuenca_test.value", self.value
        )

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            value=int(
                self.env["ir.config_parameter"]
                .sudo()
                .get_param("ucuenca_test.value", default=0)
            )
        )
        return res
