from rest_framework import serializers
from .models import  ProductcodePriceAPI

# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Productoverviewtable_3#Employee
#         fields = '__all__' #('col1' , 'col2')   


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductcodePriceAPI#Employee
        fields =  ('BR_Code' , 'P_Code' , 'MRP' , 'Sale_Rate' , 'Discount' , 'Brand' , 'BalanceQuantity')#'__all__' #('col1' , 'col2') 


class ProductQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductcodePriceAPI#Employee
        fields =  ('BR_Code' , 'P_Code' ,'BalanceQuantity')#
