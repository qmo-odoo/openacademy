from odoo import models, fields, api


class Sessions(models.Model):
    _name = 'openacademy.session'

    course_id = fields.Many2one('openacademy.course', string="Course")
    user_id = fields.Many2one('res.partner', string="Instructor", domain="[('instructor','=',True)]")
    start_date = fields.Date()
    seats = fields.Integer('Room Capacity')
    attendee_ids = fields.Many2many('res.partner', string="Attendees", domain="[('instructor','=',False)]")

    course_name = fields.Char(related="course_id.name", string="Course")
    instructor_name = fields.Char(related="user_id.name", string="Instructor")

    # _sql_constraints = [
    #     (
    #         'restrict_attendees',
    #         'CHECK(COUNT(attendee_ids) < seats)',
    #         'Not enough room for that many students'
    #     )
    # ]

    seats_filled = fields.Float(compute="_compute_seats_filled", string="Seats Taken")
    
    
    def _get_sessions_for_user(self, user):
        res = []
        for record in self:
            if user.id in record.attendee_ids:
                res.append(record.id)
        return res

    @api.depends('seats','attendee_ids')
    def _compute_seats_filled(self):
        for record in self:
            record.seats_filled = 100 * len(record.attendee_ids) / record.seats

    @api.constrains('attendee_ids')
    def _check_attendees(self):
        for record in self:
            if len(record.attendee_ids) > record.seats:
                raise models.ValidationError(
                    'Not enough room for that many students'
                )
