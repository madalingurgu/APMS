from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Staff, Product, Customer, Order, Engineering, Request
from orders.forms import OrderForm
from django.utils import timezone
from django_tables2 import RequestConfig
from orders.tables import StaffTable
from django.contrib.auth.decorators import login_required
from django.http import Http404


################################################################################
@login_required
def index(request):

    return render(request, 'index.html',)
    

################################################################################
@login_required
def order_index(request):
    myrequsts = Request.objects.all()

    return render(request, 'orders/order_index.html', {
        'myrequsts': myrequsts,
        })


################################################################################
@login_required
def order_detail(request, pk):
#    thing = get_object_or_404(Order, slug=pk,)
    thing = Request.objects.get(project_no=pk)

    return render(request, 'orders/order_detail.html',
        {'thing': thing, }
        )
        

################################################################################
@login_required
def order_edit(request, pk):
    thing3 = Request.objects.get(project_no=pk)
    form_class = OrderForm
    
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=thing3)
        if form.is_valid():
            form.save()
            return redirect('order_detail', pk=thing3.project_no)
    else:
        form = form_class(instance=thing3)
        
    return render(request, 'orders/order_edit.html', {
        'thing3': thing3,
        'form': form,
    })
    

################################################################################
@login_required
def order_create(request):
    form_class = OrderForm
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            thing4 = form.save(commit=False)
            thing4.project_no = thing4.project_no
            thing4.post_date = timezone.now()
            thing4.save()
            return redirect('order_detail', pk=thing4.project_no)
    else:
        form = form_class()
        
    return render(request, 'orders/order_create.html', {
        'form': form,
    })
    

################################################################################
@login_required
def staff(request):
    table = StaffTable(Staff.objects.all())
    RequestConfig(request).configure(table)
    
    return render(request, 'staff.html', {
            'table': table,
        })