from django.contrib import admin
from orders.models import Staff, Product, Customer, Order, Engineering, Request

class StaffAdmin(admin.ModelAdmin):
     model = Staff
     list_display = ('staff_id', 'role', 'name',)
     
class ProductAdmin(admin.ModelAdmin):
     model = Product
     list_display = ('product_id', 'p_type', 'drawing_no', 'description',
        'engineer',)
     
class CustomerAdmin(admin.ModelAdmin):
     model = Customer
     list_display = ('customer_id', 'name', 'country', 'sales_responsable',)     

class OrderAdmin(admin.ModelAdmin):
     model = Order
     list_display = ('order_id', 'quantity',)
  
class EngineeringAdmin(admin.ModelAdmin):
     model = Engineering
     list_display = ('eng_id', 'instructions',)

class RequestAdmin(admin.ModelAdmin):
    model = Request
    list_display = ('project_no', 'r_type', 'status', 'post_date',)
    

# Register your models here.
admin.site.register(Staff, StaffAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Engineering, EngineeringAdmin)
admin.site.register(Request, RequestAdmin)