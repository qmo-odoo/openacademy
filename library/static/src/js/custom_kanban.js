odoo.define('custom_kanban', function(require){
    "use strict"

    var core = require('web.core');
    
    var BasicModel = require('web.BasicModel')
    var KanbanController = require('web.KanbanController');
    var KanbanRenderer = require('web.KanbanRenderer');
    var KanbanView = require('web.KanbanView');
    var KanbanModel = require('web.KanbanModel')
    var viewRegistry = require('web.view_registry');

    var QWeb = core.qweb;


    var LibraryRentalController = KanbanController.extend({
        // renderButtons: function($node){
        //     var self = this;
        //     this._super($node)
        //     var $libraryButtons = $(qweb.render('library.GeolocalizeButton'));
        //     this.$buttons.find('.o_form_buttons_view').append($libraryButtons);
        //     this.$buttons.on('click', '.o_geolocalize', this._onGeolocalize.bind(this))
        //     this.$buttons.on('click', '.o_pay', this._onPayAmountOwed.bind(this))
        // },
        events: {
            'click .o_customer': '_onCustomerClicked',
        },
        init: function(){
            this._super.apply(this,arguments)
        },
        willStart: function () {
            var def1 = this._super.apply(this, arguments);
            var def2 = this._loadCustomers();
            return $.when(def1, def2);
        },
        reload: function (params) {
            if (this.activeCustomerID) {
                params = params || {};
                params.domain = [['customer_id', '=', this.activeCustomerID]];
            }
            var def1 = this._super(params);
            var def2 = this._loadCustomers();
            return $.when(def1, def2);
        },
        _loadCustomers: function(){
            var self = this
            
            return this._rpc({
                route: '/web/dataset/search_read',
                model: 'res.partner',
                fields: ['display_name']
            }).then(function(result){
                self.customers = result.records
                console.log(self.customers)
            })
        },
        _update: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                self.$('.o_kanban_view').prepend(QWeb.render('CustomerList', {
                    activeCustomerID: self.activeCustomerID,
                    customers: self.customers,
                }));
            });
        },
        _onCustomerClicked: function (ev) {
            this.activeCustomerID = $(ev.currentTarget).data('id');
            this.reload();
        },
        
    })

    var LibraryRentalView = KanbanView.extend({
        config: {
            Model: KanbanModel,
            Renderer: KanbanRenderer,
            Controller: LibraryRentalController
        }
    })


    viewRegistry.add('library_kanban', LibraryRentalView);
}) 