from django.forms import ModelForm
from django import forms
from orders.models import Staff, Product, Customer, Order, Engineering, Request
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset, Field
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class OrderForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-order-form'
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

        
class CustomAuthForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super(CustomAuthForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'log-in-form'
        self.helper.add_input(Submit('submit', 'Log in', css_class='btn-primary'))
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Fieldset('Please Log in', 
            Field('username', placeholder='Username',),
            Field('password', placeholder='Password',),
            )
            )