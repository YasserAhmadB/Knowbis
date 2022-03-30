from .models.Category import CategoryViewSet
from .models.Material import MaterialViewSet
from .models.Provider import ProviderViewSet
from .models.Content import ContentViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('categories', viewset=CategoryViewSet)
router.register('courses', viewset=MaterialViewSet)
router.register('instructors', viewset=ProviderViewSet)

categories_router = routers.NestedDefaultRouter(router, 'categories', lookup='category')
categories_router.register('courses', MaterialViewSet, basename='category-materials')

contents_router = routers.NestedDefaultRouter(router, 'courses', lookup='material')
contents_router.register('lectures', ContentViewSet, basename='material-contents')

urlpatterns = router.urls + categories_router.urls + contents_router.urls
