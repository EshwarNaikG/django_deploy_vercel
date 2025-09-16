
from django.contrib import admin
from django.urls import path
from store import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home , name='home'),
    path('main/', views.Main , name='main'),
    path('store/', views.Store , name='store'),
    path('cart/', views.Cart , name='cart'),
    path('checkout/', views.Checkout , name='checkout'),
    path('login/', views.Login , name='login'),
    path('about/', views.About , name='about'),
   
]
