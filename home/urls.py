from django.urls import path
from . import views

urlpatterns = [
    path('', views.TemplateView.as_view(template_name='base/base.html'), name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('signup/', views.handleSignup, name='signup'),
    path('login/', views.handleLogin, name='login'),
    path('logout/', views.handleLogout, name='logout'),

]