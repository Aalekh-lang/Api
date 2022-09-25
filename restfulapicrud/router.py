from retailerapi.viewsets import ProductViewset , ProductViewsetPrice, ProductViewsetPaymentMode,ProductQuantitySerializer_Update
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ProductPrice',ProductViewset),
router.register('ProductQuantity',ProductViewsetPrice)
router.register('ProductPaymentMode',ProductViewsetPaymentMode)
router.register('ProductUpdate',ProductQuantitySerializer_Update) 



# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrivet
