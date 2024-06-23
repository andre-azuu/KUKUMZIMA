from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import FarmerDetail, Farm, Inventory, Order, Transaction
from .forms import FarmerDetailForm, FarmForm, InventoryForm, OrderForm, TransactionForm


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



# FarmerDetail Views
def farmer_list(request):
    farmers = FarmerDetail.objects.all()
    return render(request, 'myapp/farmers_list.html', {'farmers': farmers})

def farmer_detail(request, pk):
    farmer = get_object_or_404(FarmerDetail, pk=pk)
    return render(request, 'myapp/farmer_detail.html', {'farmer': farmer})

def farmer_create(request):
    if request.method == 'POST':
        form = FarmerDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farmer_list')
    else:
        form = FarmerDetailForm()
    return render(request, 'myapp/farmer_form.html', {'form': form})

def farmer_update(request, pk):
    farmer = get_object_or_404(FarmerDetail, pk=pk)
    if request.method == 'POST':
        form = FarmerDetailForm(request.POST, instance=farmer)
        if form.is_valid():
            form.save()
            return redirect('farmer_list')
    else:
        form = FarmerDetailForm(instance=farmer)
    return render(request, 'myapp/farmer_form.html', {'form': form})

def farmer_delete(request, pk):
    farmer = get_object_or_404(FarmerDetail, pk=pk)
    if request.method == 'POST':
        farmer.delete()
        return redirect('farmer_list')
    return render(request, 'myapp/farmer_confirm_delete.html', {'farmer': farmer})


# Farm Views
def farm_list(request):
    farms = Farm.objects.all()
    return render(request, 'farm_list.html', {'farms': farms})

def farm_detail(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    return render(request, 'farm_detail.html', {'farm': farm})

def farm_create(request):
    if request.method == 'POST':
        form = FarmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farm_list')
    else:
        form = FarmForm()
    return render(request, 'farm_form.html', {'form': form})

def farm_update(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    if request.method == 'POST':
        form = FarmForm(request.POST, instance=farm)
        if form.is_valid():
            form.save()
            return redirect('farm_list')
    else:
        form = FarmForm(instance=farm)
    return render(request, 'farm_form.html', {'form': form})

def farm_delete(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    if request.method == 'POST':
        farm.delete()
        return redirect('farm_list')
    return render(request, 'farm_confirm_delete.html', {'farm': farm})
