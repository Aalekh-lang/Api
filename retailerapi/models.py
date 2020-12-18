from django.db import models

# Create your models here.

# class Employee(models.Model):
#     fullname = models.CharField(max_length=100)
#     emp_code = models.CharField(max_length=3)
#     mobile = models.CharField(max_length=15)

    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE 

class customFloatField(models.Field): 
    def db_type(self,connection):
        return 'float'

class ProductcodePriceAPI(models.Model):
    #Branch    = models.CharField(max_length=20)
    BR_Code   = models.CharField(max_length=20)
    P_Code    = models.CharField(max_length=20)
    MRP       = models.IntegerField(max_length=20)
    Sale_Rate = models.IntegerField(max_length=20)
    Discount   = models.CharField(max_length=20)
    Brand = models.CharField(max_length=20)
    BalanceQuantity   = models.IntegerField(max_length=20)

