from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from main import views as main_views
urlpatterns = [
        path('',views.custom_login, name='login'),
        path('register/', views.register, name='users-register'),
]