from rest_framework_nested import routers

from material_manager.Lecture.view import LecturesViewSet
from material_manager.Material.view import MaterialViewSet
from material_manager.Rate.view import AudienceRateMaterialViewSet
from users_manager.Audience.view import AudienceViewSet
from users_manager.Provider.view import ProviderViewSet

# router = routers.DefaultRouter()
# router.register('categories', viewset=CategoryViewSet)
# router.register('courses', viewset=MaterialViewSet)
# router.register('instructors', viewset=ProviderViewSet)
# router.register('audiences', viewset=AudienceViewSet)

# categories_router = routers.NestedDefaultRouter(router, 'categories', lookup='category')
# categories_router.register('courses', MaterialViewSet, basename='category-materials')


# contents_router = routers.NestedDefaultRouter(router, 'courses', lookup='material')
#
# contents_router.register('lectures', LecturesViewSet, basename='material-lectures')
# contents_router.register('rate', AudienceRateMaterialViewSet, basename='material-rates')

# urlpatterns = router.urls + categories_router.urls + contents_router.urls
