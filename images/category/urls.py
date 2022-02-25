print("[urls] before")
from django.urls import path, include
from . import views
print("[urls] after")

urlpatterns = [
    path('', views.category_list),
    path('<int:id>', views.category_detail),
    path('create/<str:label>', views.create_category),
]
print("[urls] after squere")
