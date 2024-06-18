from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def home1(request):
    return render(request, 'myapp1/home1.html')

def about1(request):
    return render(request, 'myapp1/about.html')

def order(request):
    return render(request, 'myapp1/order.html')

def orderHistory(request):
    return render(request, 'myapp1/orderHistory.html')

def login1(request):
    return render(request, 'myapp1/login.html')

def signup1(request):
    return render(request, 'myapp1/signup.html')

def landing1(request):
    return render(request, 'myapp1/landing.html')



