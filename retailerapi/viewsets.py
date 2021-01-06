#import requests
from rest_framework import viewsets
from . import models
from . import serializers

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