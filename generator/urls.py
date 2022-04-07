from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('password', password_page, name='password_page'),
]
