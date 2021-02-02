from django.urls import path
from . import views

urlpatterns = [
    path('', views.newshome, name='newshome'),
    path('comments/', views.comments, name='comments'),
    path('<str:slugs>/', views.newspost, name='newspost'),

]
