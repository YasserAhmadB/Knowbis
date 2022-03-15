from .views import CategoryViewSet, MaterialViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('categories', viewset=CategoryViewSet)
router.register('courses', viewset=MaterialViewSet)

urlpatterns = router.urls
