from django.shortcuts import render, redirect
from orders.models import Order

# Create your views here.

def index(request):

    orders = Order.objects.all
    test = 6

    # this is your new view and passing variable
    return render(request, 'index.html', {
        'orders': orders, 
        'test': test,
        })