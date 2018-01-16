from django.contrib import admin
from orders.models import Order, Request

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('order_number', 'customer_name',)
  

class RequestAdmin(admin.ModelAdmin):
    model = Request
    list_display = ('type_of_choice', 'order_by',)
    

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Request, RequestAdmin)


