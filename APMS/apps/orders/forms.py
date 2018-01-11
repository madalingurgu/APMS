from django.forms import ModelForm

from colection.models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('order_number', 'customer', 'drawing_number',)