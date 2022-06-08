from rest_framework_nested import routers

from .Audience.view import AudienceViewSet
from .Provider.view import ProviderViewSet

router = routers.DefaultRouter()

router.register('instructors', viewset=ProviderViewSet)
router.register('audiences', viewset=AudienceViewSet)

urlpatterns = router.urls
