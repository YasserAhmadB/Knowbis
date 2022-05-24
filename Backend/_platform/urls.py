from .models.Audience.view import AudienceViewSet
from .models.Category.view import CategoryViewSet
from .models.Material.view import MaterialViewSet
from .models.Provider.view import ProviderViewSet
from .models.Lecture.view import LecturesViewSet
from .models.Rate.view import AudienceRateMaterialViewSet

from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('categories', viewset=CategoryViewSet)
router.register('courses', viewset=MaterialViewSet)
router.register('instructors', viewset=ProviderViewSet)
router.register('audiences', viewset=AudienceViewSet)

categories_router = routers.NestedDefaultRouter(router, 'categories', lookup='category')
categories_router.register('courses', MaterialViewSet, basename='category-materials')


contents_router = routers.NestedDefaultRouter(router, 'courses', lookup='material')

contents_router.register('lectures', LecturesViewSet, basename='material-lectures')
contents_router.register('rate', AudienceRateMaterialViewSet, basename='material-rates')

urlpatterns = router.urls + categories_router.urls + contents_router.urls
