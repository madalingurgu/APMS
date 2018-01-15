from django.contrib import admin
from orders.models import Order, Request, Sample

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('order_number', 'customer_name', 'post_date',)
    prepopulated_fields = {'slug': ('order_number',)}
    
class SampleAdmin(admin.ModelAdmin):
    model = Sample
    list_display = ('description',)    


class RequestAdmin(admin.ModelAdmin):
    model = Request
    list_display = ('order', 'sample', 'order_by',)
    



# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Sample, SampleAdmin)


