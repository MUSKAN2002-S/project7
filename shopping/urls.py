from django.urls import path
from shopping.views import *
app_name='dressing'

urlpatterns=[
    path('shopping/',shopping,name='shopping')
]