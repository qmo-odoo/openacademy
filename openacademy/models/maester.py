from odoo import models, fields, api

class Maester(models.Model):
    _name = "openacademy.maester"

    name = fields.Char('Name', required=True)

    apprentice = fields.Boolean(default=True)

    class_id = fields.Many2one(
        "openacademy.class",
        string="Class to attend : "
    )