from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.material_list),
]

print("[urls] after squere")
