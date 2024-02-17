from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def home(request):
    titles = Title.objects.all()
    data = {
        'titles': titles
    }

    return render(request, 'home.html', data)


def about(request):
    return HttpResponse('about page')


def contact_page(request):
    return HttpResponse('contact page')


def movie(request):
    return HttpResponse('movie page')

