from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('social_django.urls')),
    path('logout/', views.logout, name='logout'),
]
