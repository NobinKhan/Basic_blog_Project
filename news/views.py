
from django.shortcuts import render, redirect
from .models import News, Comments
from django.contrib import messages

# Create your views here.
def newshome(request):
    news = News.objects.all().order_by('-timestamp')
    context = {
        'news': news,
    }
    return render(request, 'news/newshome.html', context)


def newspost(request, slugs):
    post = News.objects.filter(slug=slugs).first()
    comment = Comments.objects.filter(news=post)
    context = {
        'post': post,
        'comments': comment,
    }
    return render(request, 'news/newspost.html', context)


def comments(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postsn = request.POST.get('postsn')
        post = News.objects.get(sn=postsn)

        comments = Comments(comment=comment, user=user, news=post)
        comments.save()
        messages.success(request, 'Your comments has been successfully submitted')
    return redirect(request.META['HTTP_REFERER'])