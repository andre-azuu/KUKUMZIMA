from django.db import models

# Create your models here.
class buyerdb(models.Model):
    buyerUsername= models.CharField(max_length=100)
    buyerPhonenum= models.CharField(max_length=15)
    buyerPassword= models.CharField(max_length=255)
    buyerAddress=models.CharField(max_length=100)
    
    class meta:
        db_table ="buyerdb"


class Order(models.Model):
    item=models.CharField(max_length=100)
    unitPrice=models.IntegerField(max_length=100)
    buyerdb= models.ForeignKey(buyerdb, on_delete=models.CASCADE)
    status=models.BooleanField
    orderDate=models.DateField
    completeOrderDate=models.DateField

   


    # def __str__(self):
    #     return self.item

