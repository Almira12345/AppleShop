from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'shop/index.html')


def handler404p(request, exception):
    return render(request, '404.html', status=404)


def handler500p(request):
    return render(request, '404.html', status=500)
