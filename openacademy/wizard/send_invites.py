from odoo import models, fields, api

class InviteWizard(models.TransientModel):
    _name = 'openacademy.invite.wizard'

    student_ids = fields.Many2many(
        'res.partner',
        string="Students you want to invite"
    )

    current_student = fields.Many2one('res.partner')
    current_student_name = fields.Char(related="current_student.name")

    def get_active_session(self):
        #import pdb; pdb.set_trace()
        # if self.env.context.get('active_model') == 'openacademy.session':
        return self.env.context.get('active_id',False)

    session_id = fields.Many2one(
        'openacademy.session',
        string="Session",
        default=get_active_session
    )

    @api.multi
    def print_report(self):
        return self.env.ref('openacademy.report_session_invite').report_action(self)

    @api.multi
    def action_send_invites(self):
        for student in self.student_ids:
            body = self.env.ref(
                'openacademy.session_invite_template'
                ).render({
                    'name': student.name
                })
            #import pdb; pdb.set_trace()    
            self.env['mail.mail'].create({
                'subject': "Invite to a session",
                'body_html': body,
                'email_from': self.env.user.email or '',
                'email_to': student.email
            })
