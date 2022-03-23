from .views import CategoryViewSet, MaterialViewSet, ProviderViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('categories', viewset=CategoryViewSet)
router.register('courses', viewset=MaterialViewSet)
router.register('instructors', viewset=ProviderViewSet)

categories_router = routers.NestedDefaultRouter(router, 'categories', lookup='category')
categories_router.register('courses', MaterialViewSet, basename='category-materials')

urlpatterns = router.urls + categories_router.urls

