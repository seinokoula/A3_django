from django.shortcuts import render

# Create your views here.
from.models import Question


def index(request):
    return render(request, 'index.html')
