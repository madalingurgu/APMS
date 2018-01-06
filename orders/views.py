from django.shortcuts import render, redirect
from orders.models import Order

# Create your views here.

def index(request):

    orders_items = Order.objects.all

    # this is your new view and passing variable
    return render(request, 'index.html', {'orders_items': orders_items})