from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
class News(models.Model):
    sn = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    tag = models.CharField(max_length=250)
    content = RichTextField()
    photo = models.ImageField()
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

class Comments(models.Model):
    sn = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank = True, null = True, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    comment = models.TextField()
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    
