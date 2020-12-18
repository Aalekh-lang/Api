#import requests
from rest_framework import viewsets
from . import models
from . import serializers

# class EmployeeViewset(viewsets.ModelViewSet):

# 	 serializer_class = serializers.EmployeeSerializer
# 	 queryset = models.Productoverviewtable_3.objects.all()
# 	 #filter(branch=store_id)

# 	 def get_queryset(self):
# 	 	branchname = self.request.query_params.get('branchname', None)
# 	 	queryset = models.Productoverviewtable_3.objects.filter(branch=branchname)
# 	 	return queryset



class ProductViewset(viewsets.ModelViewSet):

	serializer_class = serializers.ProductSerializer
	queryset = models.ProductcodePriceAPI.objects.all()

	 #filter(branch=store_id)

	def get_queryset(self):
	 	branchname = self.request.query_params.get('BR_Code', None)
	 	queryset = models.ProductcodePriceAPI.objects.filter(BR_Code=branchname)
	 	#all()
	 	#filter(Branch=branchname)
	 	return queryset

class ProductViewsetPrice(viewsets.ModelViewSet):

	serializer_class = serializers.ProductQuantitySerializer
	queryset = models.ProductcodePriceAPI.objects.all()
	 #filter(branch=store_id)

	def get_queryset(self):
	 	branchname = self.request.query_params.get('branchname', None)
	 	queryset = models.ProductcodePriceAPI.objects.all()
	 	#filter(Branch=branchname)
	 	return queryset



#P_code wise
# def get_queryset(self):
# 	 	p_code = self.request.query_params.get('p_code', None) 
# 	 	queryset = models.Productoverviewtable_1.objects.filter(branch=p_code)
# 	 	return queryset
