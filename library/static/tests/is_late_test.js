odoo.define('is_late.tests', function(require){
    var test_utils = require('web.test_utils')

    var ListView = require('web.ListView');
    var KanbanView = require('web.KanbanView');
    var viewRegistry = require('web.view_registry');

    QUnit.module(
        'is_late',
        {
            beforeEach: function(){
                this.data = {
                    'res.partner':{
                        fields: {
                            user_id: {
                                string: 'User id',
                                type: 'many2one',
                                relation: 'res.users'
                            }
                        },
                        records: [
                            {
                                id: 1,
                                user_id: 1
                            }
                        ],
                    },
                    'product.product': {
                        fields: {
                            name: {
                                string: 'Book title',
                                type: 'char'
                            }
                        },
                        records: [
                            {
                                id: 1,
                                name: "Game of thrones"
                            },
                            {
                                id: 2,
                                name: "lord of the rings"
                            },
                            {
                                id: 3,
                                name: "lord of the rings 2"
                            }
                        ]
                    },
                    'library.rental': {
                        fields: {
                            customer_id: {
                                string:"Customer id",
                                type: "many2one",
                                relation: 'res.partner'
                            },
                            book_id: {
                                string:"Book id",
                                type: "many2one",
                                relation: 'product.product'
                            },
                            rental_date: {
                                string: "Rental date",
                                type: "date"
                            },
                            return_date: {
                                string: "Rental date",
                                type: "date"
                            },
                            is_late: {
                                string: "Is late",
                                type: 'boolean'
                            },
                            state: {
                                string: "state",
                                type: "selection",
                                selection : "[('draft', 'Draft'), ('rented', 'Rented'), ('returned', 'Returned'), ('lost', 'Lost')]"
                            }
                        },
                        records: [
                            {
                                customer_id: 1,
                                book_id: 1,
                                rental_date: "2017-09-02",
                                return_date: "2017-09-15",
                                state: "rented",
                                is_late: true
                            },
                            {
                                customer_id: 1,
                                book_id: 2,
                                rental_date: "2018-09-02",
                                return_date: "2018-09-29",
                                state: 'rented',
                                is_late: false
                            },
                            {
                                customer_id: 1,
                                book_id: 3,
                                rental_date: "2018-09-02",
                                return_date: "2018-09-29",
                                state: 'rented',
                                is_late: false
                            }
                        ]    
                    }
                }
            }
        },
        function(){
            QUnit.test('Test is_late widget', function(assert){
                assert.expect(2);
                var view = test_utils.createView({
                    View: ListView,
                    model: 'library.rental',
                    data: this.data,
                    arch: '<tree><field name="is_late" widget="FieldBoolean_custom"/></tree>',
                });
                greens = view.$el.find('.o_green')
                assert.strictEqual(view.$el.find('.o_red').length,1)
                assert.strictEqual(view.$el.find('.o_green').length,2)
            });

            QUnit.test('Test if kanban is instanciable', function(assert){
                assert.expect(3);
                var view = test_utils.createView({
                    View: KanbanView,
                    model: 'library.rental',
                    data: this.data,
                    arch: '<kanban js_class="library_kanban">' +
                    '<field name="customer_id"/>' +
                    '<field name="book_id"/>' + 
                    '<templates>'+
                      '<t t-name="kanban-box">' +
                        '<div class="oe_module_vignette oe_kanban_global_click">'+
                          '<div><field name="customer_id" /></div>' +
                          '<div><field name="book_id"/></div>'+
                        '<p>test</p>' +
                        '</div>'+
                      '</t>'+
                    '</templates>' + 
                    '</kanban>',
                    mockRPC: function(route, args){
                        if(route === "/web/dataset/search_read" && args.model === 'res.partner'){
                            assert.strictEqual(args.domain, undefined, "Search_read on all res.partner")
                            //return $.when()
                        }
                        return this._super.apply(this, arguments)
                    }
                });
                
                assert.strictEqual(view ? true : false , true)

                first = $('.o_kanban_view').find(":first")
                
                assert.strictEqual(first.hasClass("o_library_list"), true)
            
            });
        }
    ) 
})