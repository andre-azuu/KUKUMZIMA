from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing.html')


def home(request):
    return render(request, 'myapp/home.html')


def about(request):
    return render(request, 'myapp/about.html')

def farm(request):
    return render(request, 'myapp/farm.html')

def login(request):
    return render(request, 'myapp/login.html')

def signup(request):
    return render(request, 'myapp/signup.html')


def landing(request):
    return render(request, 'myapp/landing.html')