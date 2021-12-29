print("[VIEWS] before")
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
print("[VIEWS] After 1")

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
print("[VIEWS] After 2")

from .models import Category
from .serializer import CategorySerializer
from .serializer import CategorizedItemSerializer
print("[VIEWS] After 3")


@api_view()
def category_detail(request, id):
    if request.user.is_authenticated:
        category = get_object_or_404(Category, pk=id)
        serializer = CategorySerializer(category)
        print("type(serializer.data):", type(serializer.data))
        return Response(serializer.data)
    return HttpResponse("No permissions")


@api_view()
def category_list(request):
    if request.user.is_authenticated:
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        print('type(serializer):', type(serializer))
        return Response(serializer.data)
    return Response("Not authenticated")


@api_view()
def create_category(request, label: str):
    if request.user.is_authenticated:
        category = Category()
        category.label = label
        category.save()
        return Response("Saved")
    return Response("Not authenticated")