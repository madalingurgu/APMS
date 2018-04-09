from django.views.generic.base import RedirectView
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from orders import views
from orders.forms import CustomAuthForm

urlpatterns = [
################################################################################    
    url(r'^$', views.index, name='home'),
    
################################################################################         
    url(r'^orders$',
        views.order_index, name='order_index'),
    
################################################################################     
    url(r'^order-detail-(?P<pk>[-\w]+)$',
        views.order_detail, name='order_detail'),

################################################################################         
    url(r'^order-edit-(?P<pk>[-\w]+)$',
        views.order_edit, name='order_edit'),

################################################################################         
    url(r'^order-create$',
        views.order_create, name='order_create'),

################################################################################ 
    url(r'^staff/', views.staff, name='staff'),
    
################################################################################ 
    # url(r'^accounts/',
    #     include('registration.backends.default.urls')),
    
    # url('accounts/', include('django.contrib.auth.urls')),
    
    url(r'^accounts/login/$', auth_views.login, name='login', 
        kwargs={"authentication_form":CustomAuthForm}),
        
    url(r'^accounts/logout',
        include('registration.backends.default.urls')),

################################################################################ 
    url(r'^hardgear/', admin.site.urls),

]