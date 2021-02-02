from django.contrib import admin
from .models import News, Comments


class NewsAdmin(admin.ModelAdmin):
    list_display = ['sn', 'title', 'tag', 'timestamp']


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['news', 'parent', 'comment', 'user']

# Register your models here.
admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)