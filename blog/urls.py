from django.urls import path
from . import views

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('<str:slugs>/', views.blogpost, name='blogpost'),

]
