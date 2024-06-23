from django.shortcuts import render
from .models import buyerdb,Order

# Create your views here.
from django.http import HttpResponse




def buyer_list(request):
    buyers = buyerdb.objects.all()
    return render(request, 'myapp1/buyer_list.html', {'buyers': buyers})

def order(request):
    orders = Order.objects.all()
    return render(request, 'myapp1/order.html', {'orders': orders})


def home1(request):
    return render(request, 'myapp1/home1.html')

def about1(request):
    return render(request, 'myapp1/about.html')

def orderHistory(request):
    orders = Order.objects.all()
    return render(request, 'myapp1/orderHistory.html', {'orders': orders})

def login1(request):
    return render(request, 'myapp1/login.html')

def signup1(request):
    return render(request, 'myapp1/signup.html')

def landing1(request):
    return render(request, 'myapp1/landing.html')



