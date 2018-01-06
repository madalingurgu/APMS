from django.contrib import admin
from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('order_number', 'customer',)

# Register your models here.
admin.site.register(Order, OrderAdmin)