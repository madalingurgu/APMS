from django.contrib import admin
from orders.models import Order, Entry

class OrderAdmin(admin.ModelAdmin):
    model = Order
    model = Entry
    list_display = ('order_number', 'customer_name', 'post_date', 'entry',)
    prepopulated_fields = {'slug': ('order_number',)}

class EntryAdmin(admin.ModelAdmin):
    model = Entry
    list_display = ('order_type',)


# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Entry, EntryAdmin)


