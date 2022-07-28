from django.contrib import admin
from django.urls import path,include
from ecommerece_main import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('warranty_nfts',views.nftinfo, name='nfts'),
    path('order/<str:username>', views.order, name='order'),
    path('product/<str:product_id>', views.product_page, name='product_page'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
]
