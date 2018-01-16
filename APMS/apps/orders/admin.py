from django.contrib import admin
from orders.models import Order, Request

class OrderAdmin(admin.ModelAdmin):
     model = Order
     list_display = ('order_id', 'quantity', 'request_r',)
  

class RequestAdmin(admin.ModelAdmin):
    model = Request
    list_display = ('project_no', 'r_type', 'status', 'post_date', 'estimate',)
    

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Request, RequestAdmin)


