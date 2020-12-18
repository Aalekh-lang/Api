from retailerapi.viewsets import ProductViewset , ProductViewsetPrice
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ProductPrice',ProductViewset),
router.register('ProductQuantity',ProductViewsetPrice)


# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrive