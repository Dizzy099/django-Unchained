from django.shortcuts import render
from django.http import HttpResponse
from .models import Visit



def index(request, page=''):
    v = Visit(page = page)
    if request.user.is_authenticated:
        v.username = request.user.username
    v.save()
    visitors = Visit.objects.filter(page = page)
    context = {
        'count': visitors.count(),
        'page' : page,
        'visitors' : visitors,
        'name' : 'Django Unchained',
    }
    return render (request, 'index.html', context = context)

