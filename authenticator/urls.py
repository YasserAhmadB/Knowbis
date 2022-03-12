from django.urls import path, include
from . import views

# urlpatterns = [
#     path('', include('social_django.urls')),
#     path('logout/', views.logout, name='logout'),
# ]
# auth0authorization/urls.py
urlpatterns = [
    path('', include('social_django.urls')),
    path('logout/', views.logout, name='logout'),
    path('api/public', views.public),
    path('api/private', views.private),
    path('api/private-scoped', views.private_scoped),
]
