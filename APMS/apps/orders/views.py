from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order
from orders.forms import OrderForm
from django.template.defaultfilters import slugify
from django.utils import timezone

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

        
def order_edit(request, slugm):
    thing3 = Order.objects.get(slug=slugm)
    form_class = OrderForm
    
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=thing3)
        if form.is_valid():
            form.save()
            return redirect('order_detail', slugm=thing3.slug)
    else:
        form = form_class(instance=thing3)
        
    return render(request, 'order/order_edit.html', {
        'thing3': thing3,
        'form': form,
    })
    

def order_create(request):
    form_class = OrderForm
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            thing4 = form.save(commit=False)
            thing4.slug = slugify(thing4.order_number)
            thing4.post_date = timezone.now()
            thing4.save()
            return redirect('order_detail', slugm=thing4.slug)
    else:
        form = form_class()
        
    return render(request, 'order/order_create.html', {
        'form': form,
    })