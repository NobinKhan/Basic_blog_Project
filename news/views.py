from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import News

# Create your views here.
def newshome(request):
    news = News.objects.all().order_by('-timestamp')
    context = {
        'news': news,
    }
    return render(request, 'news/newshome.html', context)


def newspost(request, slugs):
    post = News.objects.filter(slug=slugs)
    context = {
        'fullpost': post,
    }
    return render(request, 'news/newspost.html', context)