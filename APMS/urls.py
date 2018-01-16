
from django.conf.urls import url, include
from django.contrib import admin
from orders import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    
    # url(r'^order-detail-(?P<pk>[-\w]+)$',
    #     views.order_detail, name='order_detail'),
        
    # url(r'^order-edit-(?P<pk>[-\w]+)$',
    #     views.order_edit, name='order_edit'),
        
    # url(r'^order-create$',
    #     views.order_create, name='order_create'),
        
    # url(r'^customer-detail-(?P<cust_name>[-\w]+)$',
    #     views.customer_detail, name='customer_detail'),

    url(r'^admin/', admin.site.urls),
]