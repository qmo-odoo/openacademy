from odoo import models, fields, api

class Course(models.Model):
    _name = "openacademy.course"

    name = fields.Char(
        string="Name of the course", 
        required=True
        )