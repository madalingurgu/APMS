from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order, Request, Engineering
# from orders.forms import OrderForm
from django.utils import timezone

# Create your views here.

def index(request):
    myrequsts = Request.objects.all()


    return render(request, 'index.html', {
        'myrequsts': myrequsts,
        })

        
# def order_detail(request, pk):
# #    thing = get_object_or_404(Order, slug=pk,)
#     thing = Order.objects.get(order_id=pk)

#     return render(request, 'order/order_detail.html',
#         {'thing': thing, }
#         )
    


# def customer_detail(request, cust_name):
# #    thing2 = get_object_or_404(Order, customer=cust_name,)
#     thing2 = Order.objects.get(customer=cust_name)

#     return render(request, 'order/customer_detail.html',
#         {'thing2': thing2, }
#         )

        
# def order_edit(request, pk):
#     thing3 = Order.objects.get(order_id=pk)
#     form_class = OrderForm
    
#     if request.method == 'POST':
#         form = form_class(data=request.POST, instance=thing3)
#         if form.is_valid():
#             form.save()
#             return redirect('order_detail', pk=thing3.order_id)
#     else:
#         form = form_class(instance=thing3)
        
#     return render(request, 'order/order_edit.html', {
#         'thing3': thing3,
#         'form': form,
#     })
    

# def order_create(request):
#     form_class = OrderForm
    
#     if request.method == 'POST':
#         form = form_class(request.POST)
#         if form.is_valid():
#             thing4 = form.save(commit=False)
#             thing4.order_id = thing4.order_id
#             thing4.post_date = timezone.now()
#             thing4.save()
#             return redirect('order_detail', pk=thing4.order_id)
#     else:
#         form = form_class()
        
#     return render(request, 'order/order_create.html', {
#         'form': form,
#     })