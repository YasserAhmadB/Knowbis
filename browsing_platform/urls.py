from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.material_list),
    path('<int:category_id>', views.material_detail),
]

print("[urls] after squere")
