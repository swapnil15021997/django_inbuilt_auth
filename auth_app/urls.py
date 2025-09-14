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
  path('api/register/', views.register_view, name='api_register'),
  path('api/login/', TokenObtainPairView.as_view(), name='api_login'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('api/logout/', views.logout_view, name='api_logout'),

  
  
]
