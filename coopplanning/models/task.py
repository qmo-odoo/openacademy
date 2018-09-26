# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Task(models.Model):
    _name = 'coopplanning.task'
    _inherit = ['mail.thread']

    name = fields.Char(track_visibility=True)
    task_template_id = fields.Many2one('coopplanning.task.template',track_visibility=True)
    task_type_id = fields.Many2one('coopplanning.task.type', string="Task Type",track_visibility=True)
    worker_id = fields.Many2one('res.partner',track_visibility=True)
    start_time = fields.Datetime(track_visibility=True)
    end_time = fields.Datetime(track_visibility=True)


    @api.model
    def create(self,values):
        new_task = super(Task,self).create(values)
        #import pdb; pdb.set_trace()
        new_task.message_subscribe(partner_ids=[new_task.worker_id.id])

        return new_task





