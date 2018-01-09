from django.contrib import admin
from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('order_number', 'customer_name', 'post_date',)
    prepopulated_fields = {'slug': ('order_number',)}

# Register your models here.
admin.site.register(Order, OrderAdmin)