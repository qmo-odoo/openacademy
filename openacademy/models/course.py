from odoo import models, fields, api

class Courses(models.Model):
    _name = 'openacademy.course'

    name = fields.Char()
    user_id = fields.Many2one('res.users', string="Responsible")

    responsible_name = fields.Char(related='user_id.name', string="Responsible")

