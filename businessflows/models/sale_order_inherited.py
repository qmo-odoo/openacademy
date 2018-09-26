from odoo import models, fields, api


class SaleOrderInherited(models.Model):
    _inherit = "sale.order"

    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('manager', 'To be confirmed by manager'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ],  string='Status',
            readonly=True,
            copy=False,
            index=True,
            track_visibility='onchange',
            default='draft')

    #state = fields.Selection(selection_add=[('manager', 'To be confirmed by manager')])


    @api.multi
    def action_to_manager(self):
        self.state = "manager"