from django.shortcuts import render, get_object_or_404


# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Material
from .serializer import MaterialSerializer


@api_view()
def material_detail(request, id):
    if request.user.is_authenticated:
        material = get_object_or_404(
            Material,
            pk=id
        )

        serializer = MaterialSerializer(
            material
        )

        return Response(serializer.data)

    return Response("No permissions")


@api_view()
def material_list(request):
    if request.user.is_authenticated:
        material = Material.objects.all()

        serializer = MaterialSerializer(
            material,
            many=True
        )

        return Response(serializer.data)
    return Response("Not authenticated")
