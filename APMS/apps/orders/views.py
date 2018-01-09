from django.shortcuts import render, redirect
from orders.models import Order
from django.urls import reverse

# Create your views here.

def index(request):

    orders = Order.objects.all
    tr_class_succes = "table-success"
    tr_class_default = "table-info"

    # this is your new view and passing variable
    return render(request, 'index.html', {
        'orders': orders, 
        'tr_class_succes': tr_class_succes,
        'tr_class_default': tr_class_default,
        })
        
def order_detail(request, order_number):
    order = Order.objects.get(order_number=order_number)
    
    
    return render(request, 'order/order_detail.html', {'order': order, })