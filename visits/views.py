from django.shortcuts import render
from django.http import HttpResponse
from .models import Visit



def index(request):
    v = Visit.objects.first()
    v.count += 1
    v.save()
    context = {
        'count': v.count,
        'name' : 'Django Unchained',
    }
    return render (request, 'index.html', context = context)

