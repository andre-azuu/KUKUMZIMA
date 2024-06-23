from django.contrib import admin
from .models import FarmerDetail, Farm, Inventory, Order, Transaction

admin.site.register(FarmerDetail)
admin.site.register(Farm)
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(Transaction)