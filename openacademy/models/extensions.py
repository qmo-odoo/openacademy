from odoo import models, fields, api

class ExtendedPartner(models.Model):
    _inherit = "res.partner"

    instructor = fields.Boolean(default=False)

    sessions_attended_ids = fields.Many2many(
        'openacademy.session',
        readonly=True
        )
