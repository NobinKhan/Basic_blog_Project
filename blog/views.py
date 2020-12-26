from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def bloghome(request):
    return render(request, 'blog/bloghome.html')


def blogpost(request, slugs):
    postnames = {}
    postnames['postname'] = slugs
    return render(request, 'blog/blogpost.html', postnames)