from django.forms import ModelForm
from django import forms
from orders.models import Staff, Product, Customer, Order, Engineering, Request

class OrderForm(ModelForm):
    class Meta:
        model = Request
        labels = {
        'project_no': 'Project number',
        'r_type': 'Type',
        }
        fields = ('project_no',
                  'r_type',
                  'product',
                  'estimate',
                  'status',
        )


    # def __init__(self, *args, **kwargs):
    #     super(OrderForm, self).__init__(*args, **kwargs)
    #     self.fields['estimate'].widget.attrs.update({
    #         'class' : 'form-control'
    #     })
    
        widgets = {
            'estimate': forms.TextInput(attrs={'type': 'email', 'class': 'form-control'}),
            'project_no': forms.TextInput(attrs={'class': 'form-control'}),
            'r_type': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }