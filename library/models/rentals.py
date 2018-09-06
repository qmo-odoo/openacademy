# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'

    customer_id = fields.Many2one('library.partner', string='Customer')
    book_id = fields.Many2one('library.book', string='Book')
    rental_date = fields.Date(string='Rental date')
    return_date = fields.Date(string='Return date')

    book_title = fields.Char(related='book_id.name', readonly=True)
    book_authors = fields.Char(related='book_id.authors_ids.name')


    renter_name = fields.Char(related="customer_id.name")
    renter_email = fields.Char(related="customer_id.email")
