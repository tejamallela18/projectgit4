from django.urls import path
from app2.views import*
app_Name='something2'

urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second')
]