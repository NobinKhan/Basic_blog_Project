from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def newshome(request):
    return render(request, 'news/newshome.html')


def newspost(request, slugs):
    postnames = {}
    postnames['postname'] = slugs
    return render(request, 'news/newspost.html', postnames)