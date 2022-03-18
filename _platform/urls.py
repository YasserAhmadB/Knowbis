from .views import CategoryViewSet, MaterialViewSet, ProviderViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('categories', viewset=CategoryViewSet)
router.register('courses', viewset=MaterialViewSet)
router.register('instructors', viewset=ProviderViewSet)

urlpatterns = router.urls
