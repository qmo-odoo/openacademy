odoo.define('home_message', function(require){
    "use strict"

    var appSwitcher = require('web_enterprise.AppSwitcher')

    appSwitcher.include({
        render: function(){

            this._super.apply(this,arguments)
            this.$child = this.$el.find($('.o_menu_search'))
            
            if (moment().isoWeekday() === 1) {
                this.$el.find($('.alert')).remove()
                this.$child.after('<div class="alert alert-warning">Do not forget about the promotion</div>')
            }
        }
    })
}) 