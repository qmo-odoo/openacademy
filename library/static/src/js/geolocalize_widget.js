odoo.define('library.form_view', function(require){
    var core = require('web.core');
    
    var BasicModel = require('web.BasicModel')
    var FormController = require('web.FormController');
    var FormRenderer = require('web.FormRenderer');
    var FormView = require('web.FormView');
    var viewRegistry = require('web.view_registry');

    var qweb = core.qweb;

    var LibraryCustomerController = FormController.extend({
        renderButtons: function($node){
            var self = this;
            this._super($node)
            var $libraryButtons = $(qweb.render('library.GeolocalizeButton'));
            this.$buttons.find('.o_form_buttons_view').append($libraryButtons);
            if(this.model.get(this.handle, {raw:true}).data.amount_owed === 0){
                this.$buttons.find('.o_pay').remove()
            }
            this.$buttons.on('click', '.o_geolocalize', this._onGeolocalize.bind(this))
            this.$buttons.on('click', '.o_pay', this._onPayAmountOwed.bind(this))
        },
        
        _onGeolocalize: function(){
            var self = this
            partner_id = this.model.get(this.handle, {raw:true}).res_id
            if(this.model.get(this.handle, {raw:true}).data.amount_owed !== 0){
                this._rpc({
                    model: 'res.partner',
                    method: 'geo_localize',
                    args: [partner_id]
                }).then(function () {
                    self.reload();
                });
            }   
        },

        _onPayAmountOwed: function(){
            var self = this;
            partner_id = this.model.get(this.handle, {raw:true}).res_id
            this._rpc({
                model: 'res.partner',
                method: 'pay_amount_owed',
                args: [partner_id]
            }).then(function () {
                self.reload();
            });
        }
    })

    var LibraryCustomerView = FormView.extend({
        config: {
            Model: BasicModel,
            Renderer: FormRenderer,
            Controller: LibraryCustomerController
        }
    })


    viewRegistry.add('library_customer', LibraryCustomerView);
})