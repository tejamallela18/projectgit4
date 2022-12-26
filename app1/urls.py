from django.urls import path
from app1.views import *
app_Name='something1'

urlpatterns=[
    path('first/',first,name='first'),
    path('second',second,name='second'),
]
