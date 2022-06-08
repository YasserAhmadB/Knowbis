from rest_framework_nested import routers

from category_manager.Category.view import CategoryViewSet

router = routers.DefaultRouter()
router.register('categories', viewset=CategoryViewSet)

urlpatterns = router.urls
