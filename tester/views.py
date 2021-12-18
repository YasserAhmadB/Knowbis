from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
def home(request):
    s = "Not logged in"
    if request.user.is_authenticated:
        s = "Logged in"
    return HttpResponse(str(s))