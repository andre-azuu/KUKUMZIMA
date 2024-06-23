from django import forms
from .models import FarmerDetail, Farm, Inventory, Order, Transaction

class FarmerDetailForm(forms.ModelForm):
    class Meta:
        model = FarmerDetail
        fields = '__all__'

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = '__all__'

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
