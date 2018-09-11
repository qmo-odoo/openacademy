# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Books(models.Model):
    _inherit = 'product.product'

    author_ids = fields.Many2many(
        comodel_name="res.partner",
        string="Authors",
        domain=[('author','=',True), ],
    )
    edition_date = fields.Date(string='Edition date',)
    isbn = fields.Char(string='ISBN')
    publisher_id = fields.Many2one(
        'res.partner',
        string='Publisher',
        domain=[('publisher','=',True), ],
    )
    rental_ids = fields.One2many(
        'library.rental',
        'book_id',
        string='Rentals',)
    book = fields.Boolean('is a book', default=False)

    rental_count = fields.Integer(compute="_compute_rental_count")
    
    @api.depends('rental_ids')
    def _compute_rental_count(self):
        self.rental_count = len(self.rental_ids)

    @api.multi
    def action_get_rentals_infos(self):

        partner_ids = []
        for rental in self.rental_ids:
            partner_ids.append(rental.customer_id.id)

        return {
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'res.partner',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'new',
            'domain': [('id', 'in', partner_ids)]
        }


class BookLoanWizard(models.TransientModel):
    _name = "library.wizard"

    book_ids = fields.Many2many('product.product',domain="[('book','=',True)]")
    partner_id = fields.Many2one('res.partner', )

    rental_date =  fields.Date(string='Rental date', default=lambda self: fields.Date.today())
    return_date =  fields.Date(string='Return date')

    wizard_step1 = fields.Boolean(default=False)
    

    @api.multi
    def next(self):
        self.wizard_step1 = True
        return {
            "type": "ir.actions.do_nothing"
        } 
    
    @api.multi
    def cancel(self):
        self.wizard_step1 = False
        return {
            "type": "ir.actions.do_nothing"
        } 
        

    @api.multi
    def submit(self):
        for book in self.book_ids:
            values = {
                'book_id' : book.id,
                'customer_id': self.partner_id.id,
                'rental_date': self.rental_date,
                'return_date': self.return_date
            }
            self.env['library.rental'].create(values)



