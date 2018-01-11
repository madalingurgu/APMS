from django.shortcuts import render, get_object_or_404
from orders.models import Order

# Create your views here.

def index(request):

    orders = Order.objects.all()
    tr_class_succes = "table-success"
    tr_class_default = "table-info"

    return render(request, 'index.html', {
        'orders': orders, 
        'tr_class_succes': tr_class_succes,
        'tr_class_default': tr_class_default,
        })

        
def order_detail(request, slugm):
#    thing = get_object_or_404(Order, slug=slugm,)
    thing = Order.objects.get(slug=slugm)

    return render(request, 'order/order_detail.html',
        {'thing': thing, }
        )

def customer_detail(request, cust_name):
#    thing2 = get_object_or_404(Order, customer_name=cust_name,)
    thing2 = Order.objects.get(customer_name=cust_name)

    return render(request, 'order/customer_detail.html',
        {'thing2': thing2, }
        )

        
def order_edit(request):

    return render(request, 'order/edit_order.html',
    
        )