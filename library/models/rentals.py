# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, http, _
import werkzeug
from datetime import datetime

class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'
    _order = "rental_date desc,return_date desc"

    customer_id = fields.Many2one(
        'res.partner',
        'Customer',
        domain=[('customer','=',True), ],
        required=True,
    )
    book_id = fields.Many2one(
        'product.product',
        'Book',
        domain=[('book','=',True)],
        required=True,
    )
    rental_date = fields.Date(string='Rental date', required=True, default=lambda self: fields.Date.today())
    return_date = fields.Date(string='Return date', required=True)


class RentalsController(http.Controller):



    @http.route('/library/rentals', auth='public', website=True)
    def index(self, **kw):
        rentals = http.request.env['library.rental'].search([])
        rentals_book_ids = [r.book_id for r in rentals] 
        books = http.request.env['product.product'].search([('book','=',True)])
        valid_books = [b for b in books if b not in rentals_book_ids]
        # import pdb; pdb.set_trace()
        return http.request.render('library.rental_page_template', {
            'books': valid_books
        })

    #Get
    @http.route('/library/rentals/<int:id>', website=True)
    def rental(self, id):
        book = http.request.env['product.product'].search([('id', '=', id)])
        
        rental_data = {
            'book_id': book.id,
            'customer_id': http.request.env.user.id,
            'rental_date': datetime.today(),
            'return_date': datetime.today() 
        }
         
        return http.request.render('library.rental_page_form_template', {
            'book': book,
            'data': rental_data
        })

    #Post
    @http.route('/library/rentals/<int:id>', methods=['POST'], auth="public", csrf=False)
    def confirm_rental(self,id, **kw):
        user = http.request.env.user.id
        values = {
            'book_id': id,
            'customer_id': user,
            'rental_date': kw['rental_date'],
            'return_date': kw['return_date']
        }
        # import pdb; pdb.set_trace()
        http.request.env['library.rental'].create(values)

        return werkzeug.utils.redirect('/library/rentals')
