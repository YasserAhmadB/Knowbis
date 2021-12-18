from django.conf import settings
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from category.models import Category
from category.serializer import CategorySerializer


@api_view()
def category_detail(request, id):
    category = get_object_or_404(Category, pk=id)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view()
def category_list(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)
