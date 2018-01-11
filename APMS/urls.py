
from django.conf.urls import url, include
from django.contrib import admin
from orders import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    
    url(r'^order-number/(?P<slugm>[-\w]+)/$',
        views.order_detail, name='order_detail'),
        
    url(r'^order-number/edit/(?P<slugm>[-\w]+)/$',
        views.order_edit, name='order_edit'),
        
    url(r'^customer-details/(?P<cust_name>[-\w]+)/$',
        views.customer_detail, name='customer_detail'),
        
    url(r'^order/',
        views.order_edit, name='order_edit'),
    
    url(r'^admin/', admin.site.urls),
]