from rest_framework_nested import routers

from category_manager.urls import router
from .Lecture.view import LecturesViewSet
from .Material.view import MaterialViewSet
from .Rate.view import AudienceRateMaterialViewSet

router.register('courses', viewset=MaterialViewSet)

categories_router = routers.NestedDefaultRouter(router, 'categories', lookup='category')
categories_router.register('courses', MaterialViewSet, basename='category-materials')

contents_router = routers.NestedDefaultRouter(router, 'courses', lookup='material')

contents_router.register('lectures', LecturesViewSet, basename='material-lectures')
contents_router.register('rate', AudienceRateMaterialViewSet, basename='material-rates')

urlpatterns = router.urls + categories_router.urls + contents_router.urls
