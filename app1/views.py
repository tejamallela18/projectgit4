from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('this is app1 view1')
def second(request):
    return HttpResponse('this is app1 view2')