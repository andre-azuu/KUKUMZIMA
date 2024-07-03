from django.db import models

class FarmerDetail(models.Model):
    dbfarmerUsername = models.CharField(max_length=100)
    dbfarmerPhonenum = models.CharField(max_length=15)
    dbfarmerPassword = models.CharField(max_length=255)
    dbfarmerEmail = models.CharField(max_length=100)
    dbfarmerAddress = models.CharField(max_length=100)

    class Meta:
        db_table = "farmer"

class Farm(models.Model):
    farmlocation = models.CharField(max_length=255)
    numberOfHens = models.IntegerField()
    productionRate = models.DecimalField(max_digits=5, decimal_places=2)
    profitLoss = models.DecimalField(max_digits=10, decimal_places=2)
    productivity = models.DecimalField(max_digits=5, decimal_places=2)
    farmer_detail = models.ForeignKey(FarmerDetail, on_delete=models.CASCADE)

    class Meta:
        db_table = "farm"

class Inventory(models.Model):
    quantityOfEggs = models.IntegerField()
    unitPrice = models.IntegerField()
    numberOfHens = models.IntegerField()
    farmer_detail = models.ForeignKey(FarmerDetail, on_delete=models.CASCADE)

class Order(models.Model):
    item = models.CharField(max_length=100)
    unitPrice = models.IntegerField()
    farmer_detail = models.ForeignKey(FarmerDetail, on_delete=models.CASCADE)
    status = models.BooleanField()
    orderDate = models.DateField()
    completeOrderDate = models.DateField()

class Transaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amountPaid = models.IntegerField()
    transactionDate = models.DateField()
    status = models.BooleanField()
