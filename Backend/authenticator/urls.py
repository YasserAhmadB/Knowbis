from django.urls import path
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register('users', viewset=views.UserViewSet)

urlpatterns = [
    path('api/private/', views.private),
    path('api/public/', views.public),
    path('api/private-scoped/', views.private_scoped),
] + router.urls
