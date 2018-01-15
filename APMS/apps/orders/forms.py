from django.forms import ModelForm

from orders.models import Order, Request

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('order_number', 'customer_name', 'drawing_number', 'request_type',)