from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from category.models import Category
from category.serializer import CategorySerializer


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
