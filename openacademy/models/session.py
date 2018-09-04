from odoo import models,fields,api

class Session(models.Model):
    _name = "openacademy.session"

    session_ready = fields.Boolean(string="The session is ready : ",default=False)

    session_start = fields.Date(string="The session will start on the : ", required=True)
    session_end = fields.Date(string="The session will end on the : ", required=True)

    maester_id = fields.Many2one(
        "openacademy.maester",
        string="Maester in charge"
    )

    attendees_ids = fields.Many2many(
        "openacademy.maester",
        string="Attendees : "
    )

    course_id = fields.Many2one(
        "openacademy.course",
        string="Course : ",
        ondelete="cascade",
        required=True
        )