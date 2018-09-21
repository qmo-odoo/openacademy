
odoo.define('int_widget', function(require){
    var fieldRegistry = require('web.field_registry')
    var basic_fields = require('web.basic_fields')
    var relational_fields = require('web.relational_fields')

    var custom_integer = basic_fields.FieldInteger.extend({    
        init: function () {
            this._super.apply(this, arguments);
        },

        _render: function(){
            this._super()
            text = this.$el.text()
            this.$el.html(text.replace(',',''));
        }
    })

    var custom_boolean = basic_fields.FieldBoolean.extend({
        template: "toggle_button",
        supportedFieldTypes: ['boolean'],
        init: function(){
            this._super.apply(this, arguments);
        },

        _render: function(){
            this._super()
            
            if(this.value){
                this.$el.empty().append('<i class="fa fa-circle o_red" style="color:red"></i>')
            }
            else{
                this.$el.empty().append('<i class="fa fa-circle o_green" style="color:green"></i>')
            }
           
            
        }


    })

    var custom_many2one = relational_fields.FieldMany2One.extend({
        
        init: function(){
            this._super.apply(this, arguments);
        },

        _render: function(){
            this._super()
            console.log(this.recordData)
            this.$el.children('#alert').remove()
            if(this.recordData.amount_owed > 10 && this.recordData.amount_owed < 20){
                this.$el.append('<div id="alert" class="alert alert-warning">Warning</div>')
            }
            else if(this.recordData.amount_owed >= 20) {
                this.$el.append('<div id="alert" class="alert alert-danger">Danger</div>')
            }
    }})

    fieldRegistry.add('FieldInteger_custom', custom_integer)
    fieldRegistry.add('FieldBoolean_custom', custom_boolean)
    fieldRegistry.add('FieldM2O_custom', custom_many2one)

    return {
        'FieldInteger_custom': custom_integer,
        'FieldBooelan_custom': custom_boolean
    }
})