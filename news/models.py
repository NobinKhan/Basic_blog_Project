from django.db import models

# Create your models here.
class News(models.Model):
    sn = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    tag = models.CharField(max_length=250)
    content = models.TextField()
    photo = models.ImageField()
    slug = models.CharField(max_length=250)
    timestamp = models.TimeField(auto_now=True)


