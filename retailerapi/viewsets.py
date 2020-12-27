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
	 	queryset = models.productcodepriceapi.objects.filter(BR_Code=branchname)
	 	#all()
	 	#filter(Branch=branchname)
	 	return queryset

class ProductViewsetPrice(viewsets.ModelViewSet):

	serializer_class = serializers.ProductQuantitySerializer
	queryset = models.productcodepriceapi.objects.all()
	 #filter(branch=store_id)

	def get_queryset(self):
	 	branchname = self.request.query_params.get('branchname', None)
	 	queryset = models.productcodepriceapi.objects.all()
	 	#filter(Branch=branchname)
	 	return queryset


class ProductViewsetPaymentMode(viewsets.ModelViewSet):

	serializer_class = serializers.ProductPaymentModeSerializer
	queryset = models.productrevenuedeatils_paymentmode.objects.all()
	 #filter(branch=store_id)

	# def get_queryset(self):
	#  	branchname = self.request.query_params.get('branchname', None)
	#  	queryset = models.productrevenuedeatils_paymentmode.objects.filter(BR_Code=branchname)
	#  	#filter(Branch=branchname)
	#  	return queryset