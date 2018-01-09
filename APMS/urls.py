from django.conf.urls import url
from django.contrib import admin
from orders import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    
    url(r'^order/order_number', views.order_detail, name='order_detail'),
    
    
    
    url(r'^admin/', admin.site.urls),
]
