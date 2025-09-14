from django.contrib import admin
from django.urls import path,include
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
  path('register',views.register_view,name='register'),
  path('login',views.login_view,name='login'),
  path('logout',views.logout_view ,name='logout_view'),
  path('dashboard',views.home,name='dashboard'),
  path('prod-list',views.p_list,name='prod-list'),
 
  
  path('api/register/', views.register_view, name='api_register'),
  path('api/login/', TokenObtainPairView.as_view(), name='api_login'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('api/logout/', views.logout_view, name='api_logout'),


  path('api/product-list/', views.product_list, name='product_list'),


path('api/product-save/', views.product_save, name='product_save'),

  path('api/product-remove/', views.product_remove, name='product_remove'),

  
  
]
