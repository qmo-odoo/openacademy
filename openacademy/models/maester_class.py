from odoo import models, fields, api

class MaesterClass(models.Model):
    _name = "openacademy.class"

    level = fields.Integer(required=True, default=1, string="Class level")

    maester_ids = fields.One2many(
        "openacademy.maester",
        "class_id",
        required=True
    )