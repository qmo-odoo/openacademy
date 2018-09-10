# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Partner(models.Model):
    _inherit = 'res.partner'

    author =  fields.Boolean('is an Author', default=False)
    publisher =  fields.Boolean('is a Publisher', default=False)
    rental_ids = fields.One2many(
        'library.rental',
        'customer_id',
        string='Rentals')
    book_ids = fields.Many2many(
        comodel_name="product.product",
        string="Books",
        domain=[('book','=',True), ],
    )
    nationality_id = fields.Many2one(
        'res.country',
        'Nationality',
    )
    birthdate =  fields.Date('Birthdate')


    currency_id = fields.Many2one(
        'res.currency',
        compute="_get_currency"
    )

    debt = fields.Monetary(
        compute="_compute_debt",
        currency_field='currency_id',
        string="Loan price"
        )



    
    
    @api.depends('rental_ids')
    def _get_currency(self):
        for record in self:
            if record.rental_ids[0]:
                record.currency_id = record.rental_ids[0].book_id.currency_id.id

            

    @api.depends('rental_ids','rental_ids.cleared')
    def _compute_debt(self):
        for record in self:
            record.debt = 0
            for rental in record.rental_ids:
                if not record.currency_id:
                    record.currency_id = record.rental_ids[0].book_id.currency_id.id
                if not rental.cleared:
                    record.debt += rental.book_id.lst_price

