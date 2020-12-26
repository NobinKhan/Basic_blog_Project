from django.shortcuts import render
from .models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def contact(request):
    messages.success(request, "hello everyone")
    print(messages.error(request, "hi baby"))
    print(messages.ERROR)
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')