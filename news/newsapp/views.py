from django.shortcuts import render

from newsfetch.google import google_search
from newsfetch.news import newspaper
from .models import *
# Create your views here.


def home(request):

    return render(request, 'home.html')

def search(request):
    if request.method == 'GET':
        title = request.GET['title']
        data= News.objects.filter(headline=title)

        context = {
            'data':data
        }

    return render(request, 'list.html', context)