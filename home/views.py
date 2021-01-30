from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from news.models import News

# Create your views here.

    
def home(request):
    news = News.objects.all().order_by('-timestamp')
    context = {
        'news': news,
    }
    return render(request, 'home/home.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<3 or len(email)<3 or len(phone)<10 or len(content)<4 :
            messages.error(request, "Please fill up the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Successfully Submitted")
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')


def search(request):
    try:
        if request.method != 'POST':
            messages.error(request, "Please fill up the form correctly!")
            return redirect(request.META['HTTP_REFERER'])
        search = request.POST['search']
        if search == '' or str.__len__(search) > 50:
            context = {
                'search':search,
            }
            return render(request, 'home/search.html', context)
        result = News.objects.filter(tag__icontains=search)
        context = {
            'news':result,
            'search':search,
        }
        return render(request, 'home/search.html', context)
    except:
        return render(request, 'home/search.html')


def handleSignup(request):
    # request validation
    try:
        if request.method != 'POST':
            messages.error(request, "Please fill up the form correctly!")
            return redirect(request.META['HTTP_REFERER'])


        #  collect User information
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

            # form validation
        if password1 != password2:
            messages.error(request, "Password didn't match! please try again.")
            return redirect(request.META['HTTP_REFERER'])  
        if not username.isalnum():
            messages.error(request, "Username should only contain lowercase letters and numbers without any special charecter.")
            return redirect(request.META['HTTP_REFERER']) 

            # create user  
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect(request.META['HTTP_REFERER'])
    except:
        return render(request, 'home/home.html')


def handleLogin(request):
    try:
        if request.method != 'POST':
            messages.error(request, "Please fill up the form correctly!")
            return redirect(request.META['HTTP_REFERER'])

        #  collect User information
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        # validating user information
        user = authenticate(username=loginusername, password=loginpassword)

        # saving user information
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, "Username or Password is not matched. Please try again !")
            return redirect(request.META['HTTP_REFERER'])
    except:
        return render(request, 'home/home.html')


def handleLogout(request):
    try:
        logout(request)
        messages.success(request, "Successfully log out!")
        return redirect(request.META['HTTP_REFERER'])
    except:
        return render(request, 'home/home.html')