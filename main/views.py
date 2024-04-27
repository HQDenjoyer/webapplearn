from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

