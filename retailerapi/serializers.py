from rest_framework import serializers
from .models import  productcodepriceapi,productrevenuedeatils_paymentmode

# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Productoverviewtable_3#Employee
#         fields = '__all__' #('col1' , 'col2')   


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = productcodepriceapi#Employee
        fields =  ('BR_Code' , 'P_Code' , 'MRP' , 'Sale_Rate' , 'Discount' , 'Brand' , 'BalanceQuantity','Retailer_ID')#'__all__' #('col1' , 'col2') 


class ProductQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = productcodepriceapi#Employee
        fields =  ('BR_Code' , 'P_Code' ,'BalanceQuantity','Retailer_ID')# 

class ProductPaymentModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = productrevenuedeatils_paymentmode#Employee
        fields =  ('BR_Code' , 'TransactionNumber' ,'SaleAmount', 'Narration','Retailer_ID')

  
class ProductQuantitySerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = productcodepriceapi#Employee
        fields =  ('BR_Code' , 'P_Code' ,'BalanceQuantity','Retailer_ID')
