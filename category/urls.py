from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:id>', views.category_detail),
    path('all/', views.category_list),
]
