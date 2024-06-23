from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class FarmerDetail(models.Model):
    dbfarmerUsername = models.CharField(max_length=100)
    dbfarmerPhonenum = models.CharField(max_length=15)
    dbfarmerPassword = models.CharField(max_length=255)
    dbfarmerEmail = models.EmailField(max_length=100)
    dbfarmerAddress = models.CharField(max_length=100)

    class Meta:
        db_table = "farmer"

class Farm(models.Model):
    farmlocation = models.CharField(max_length=255)
    farmer_detail = models.ForeignKey(FarmerDetail, on_delete=models.CASCADE)

class Inventory(models.Model):
    quantityOfEggs = models.PositiveIntegerField()
    unitPrice = models.PositiveIntegerField()
    numberOfHens = models.PositiveIntegerField()
    farmer_detail = models.ForeignKey(FarmerDetail, on_delete=models.CASCADE)

class Order(models.Model):
    item = models.CharField(max_length=100)
    unitPrice = models.PositiveIntegerField()
    farmer_detail = models.ForeignKey(FarmerDetail, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    orderDate = models.DateField()
    completeOrderDate = models.DateField(null=True, blank=True)

class Transaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amountPaid = models.PositiveIntegerField()
    transactionDate = models.DateField()
    status = models.BooleanField(default=False)
