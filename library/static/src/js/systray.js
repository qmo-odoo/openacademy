odoo.define('library.systray', function(require){
    "use strict"

    var config = require('web.config');
    var core = require('web.core');
    var framework = require('web.framework');
    var session = require('web.session');
    var SystrayMenu = require('web.SystrayMenu');
    var Widget = require('web.Widget');

    

    var QWeb = core.qweb;

    var InputMenu = Widget.extend({
        template: 'library.systray_input',
        sequence: 10,
        events: {
            'input .o_input': '_onInput'
        },

        init: function(){
            this._super.apply(this,arguments)
            $('.dropdown-menu  li').click(function(e) {
                e.stopPropagation();
            });
        },

        start: function(){
            this._super.apply(this,arguments)
            $('.dropdown-menu  li').click(function(e) {
                e.stopPropagation();
            });
        },
       
        _onInput: function(){
            var id = parseInt(this.$('.o_input').val())
            if(!_.isNaN(id)){
                this.do_action('library.action_customer_form', {
                    res_id: id
                })
            }
        }
        
        
    })

    SystrayMenu.Items.push(InputMenu)
}) 