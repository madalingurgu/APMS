from django.forms import ModelForm
from django import forms
from orders.models import Staff, Product, Customer, Order, Engineering, Request
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset, Field
from django.urls import reverse


class OrderForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-order-form'
        # self.helper.form_method = 'post'
        # self.helper.form_action = reverse('order_create')
        self.helper.add_input(Submit('submit', 'Save', css_class='btn-success'))
        self.helper.layout = Layout(
            Fieldset('', 
            Field('project_no', placeholder='Please input the project number!',),
            'r_type',
            'product',
            'customer',
            'order',
            'eng',
            'responsable',
            'request_date',
            'estimate',
            'status',
            'comments',
            style="color:black;",
            )    
            
            
            # self.helper.label_class = 'col-md-2'
            # self.helper.layout = Layout(
            # Field('project_no', style="color: brown;", 
            #     placeholder='Please input the project number!',),
            # Field('r_type', style="color: brown;",),
            # Fieldset('', 'product', 'estimate', style="color: black;"),
            # HTML("""<h3>Create new customers account</h3>"""),
            # Row(Field('first_name',),),
            # Field('project_no', placeholder='Your first name', css_class="some-class")
            # Div('last_name', title="Your last name")
            )
    class Meta:
        model = Request
        labels = {
        'project_no': 'Project number',
        'r_type': 'Type',
        }
        fields = ('project_no',
                  'r_type',
                  'product',
                  'customer',
                  'order',
                  'eng',
                  'responsable',
                  'request_date',
                  'estimate',
                  'status',
                  'comments',
        )
        # widgets = {
        #     'project_no':TextInput(attrs={'size':'70','cols': 10, 'rows': 20}),  
        # }