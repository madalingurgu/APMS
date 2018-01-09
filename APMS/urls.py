
from django.conf.urls import url, include
from django.contrib import admin
from orders import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    
    url(r'^order/(?P<slug>[-\w]+)/$',
        views.order_detail, name='order_detail'),
    
    
    
    url(r'^admin/', admin.site.urls),
]
