from odoo import models, fields, api

class ProjectTaskInherited(models.Model):
    _inherit = "project.task"

    @api.multi
    def write(self, values):
        res = super(ProjectTaskInherited, self).write(values)
        if 'timesheet_ids' in values and self.remaining_hours < 0:
            msg = self.env['mail.mail'].create({
                    'subject': 'Issues for the task',
                    'email_to': self.manager_id.email,
                    'body_html': "<p>Test</p>",
                    'body': "<p>Test</p>",
                })
            self.env['mail.mail'].send(msg)
        return res
