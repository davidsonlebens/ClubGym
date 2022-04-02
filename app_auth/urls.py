from django.urls import path
from .views import *

urlpatterns=[
    path('login', login_gym, name='login-gym'),
    path('register', register, name='register'),
    path('logout', logout_gym, name='logout'),
]