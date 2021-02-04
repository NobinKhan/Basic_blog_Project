
from django.shortcuts import render, redirect
from .models import News, Comments
from django.contrib import messages
from news.templatetags import extras

# Create your views here.
def newshome(request):
    news = News.objects.all().order_by('-timestamp')
    context = {
        'news': news,
    }
    return render(request, 'news/newshome.html', context)


def newspost(request, slugs):
    post = News.objects.filter(slug=slugs).first()
    comment = Comments.objects.filter(news=post, parent=None).order_by('-timestamp')
    replies = Comments.objects.filter(news=post).order_by('-timestamp').exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sn not in replyDict.keys():
            replyDict[reply.parent.sn] = [reply]
        else:
            replyDict[reply.parent.sn].append(reply)
    context = {
        'post': post,
        'comments': comment,
        'replies': replyDict,
    }
    return render(request, 'news/newspost.html', context)


def comments(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postsn = request.POST.get('postsn')
        post = News.objects.get(sn=postsn)
        parentsn = request.POST.get('parentsn')
        parent = Comments.objects.get(sn=parentsn)

        if parentsn == '':
            comments = Comments(comment=comment, user=user, news=post)
            comments.save()
            messages.success(request, 'Your comments has been successfully submitted')
        else:
            comments = Comments(comment=comment, user=user, news=post, parent=parent)
            comments.save()
            messages.success(request, 'Your reply has been successfully submitted')
    return redirect(request.META['HTTP_REFERER'])