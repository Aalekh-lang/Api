#import requests
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from django.db import  transaction
import psycopg2

class ProductViewset(viewsets.ModelViewSet):

	serializer_class = serializers.ProductSerializer
	queryset = models.productcodepriceapi.objects.all()

	 #filter(branch=store_id)

	def get_queryset(self):
	 	branchname = self.request.query_params.get('BR_Code', None)
	 	Retailerid = self.request.query_params.get('Retailerid', None)
	 	queryset = models.productcodepriceapi.objects.filter(BR_Code=branchname,Retailer_ID=Retailerid)
	 	#all()
	 	#filter(Branch=branchname)
	 	return queryset

class ProductViewsetPrice(viewsets.ModelViewSet):

	serializer_class = serializers.ProductQuantitySerializer
	queryset = models.productcodepriceapi.objects.all()
	 #filter(branch=store_id)

	def get_queryset(self):
	 	branchname = self.request.query_params.get('branchname', None)
	 	Retailerid = self.request.query_params.get('Retailerid', None)
	 	queryset = models.productcodepriceapi.objects.filter( BR_Code=branchname ,Retailer_ID=Retailerid) #,Retailer_ID=Retailer_ID
	 	#filter(Branch=branchname)
	 	print(queryset)
	 	return queryset


class ProductViewsetPaymentMode(viewsets.ModelViewSet):

	serializer_class = serializers.ProductPaymentModeSerializer
	queryset = models.productrevenuedeatils_paymentmode.objects.all()
	 #filter(branch=store_id)

	def get_queryset(self):
	 	branchname = self.request.query_params.get('branchname', None)
	 	Retailerid = self.request.query_params.get('Retailerid', None)
	 	queryset = models.productrevenuedeatils_paymentmode.objects.filter(BR_Code=branchname,Retailer_ID=Retailerid)
	 	#filter(Branch=branchname)
	 	return queryset


class ProductQuantitySerializer_Update(viewsets.ModelViewSet):
	
	serializer_class = serializers.ProductQuantitySerializerUpdate
	queryset = models.productcodepriceapi.objects.all()
	def get_queryset(self):
		branchname = self.request.query_params.get('BR_Code', None)
		Retailerid = self.request.query_params.get('Retailerid', None) 
		Productid = self.request.query_params.get('Productid', None)
		balancequantity = self.request.query_params.get('BalanceQuantity', None)
		queryset = models.productcodepriceapi.objects.filter(BR_Code=branchname,Retailer_ID=Retailerid,P_Code=Productid)#.select_for_update().get() #update(BR_Code="THN1")
		#Connection
		conn = psycopg2.connect("host=ec2-34-193-44-192.compute-1.amazonaws.com dbname=d9ico489bsvs8l user=kybxasjbluxvel password=3d48454bfa4eb31d09f583cdac569004dd40d380bfdd22a0485a2c4adc84c742")
		cur = conn.cursor()
		sql = '''Update retailerapi_productcodepriceapi set  "BalanceQuantity" = '%s' where "BR_Code" = '%s' and "Retailer_ID" = %s and "P_Code" = '%s' '''
		cur.execute(sql % (balancequantity,branchname ,Retailerid ,Productid))
		conn.commit()
		return queryset
