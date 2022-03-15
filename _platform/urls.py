from .views import CategoryViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('categories', viewset=CategoryViewSet)

urlpatterns = router.urls
