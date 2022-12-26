from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('this view is app2 view1')
def second(request):
    return HttpResponse('this view is app2 view2')