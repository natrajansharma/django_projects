import email
from pyexpat.errors import messages
from django.forms import models
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

# Create your views here.

# Admin - natrajansharma - NaTrajan@86


def base(request):
    return render(request, "base.html")

# @login_required(login_url='/login')


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html", {'price': 56999})


def loginusers(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
     #   print(username, password)

       # user = User.objects.get(username = username)
      #  print(user)
        # check if user has eneterded correct credentials

        user = authenticate(username=username, password=password)

        if user is not None:

            # A bacekend authenticated the credentials

            login(request, user)
            return redirect("/")

        else:

            # No backed auhenticated the credentials

            return render(request, "login.html")

    return render(request, "login.html")


def logoutusers(request):
    logout(request)
    request.session.clear()
    return redirect("/login")


def signupusers(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Already Exist')
            return redirect('/signup')

        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Already Exist')
            return redirect('/signup')
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                        username=username, email=email, password=password)
      #  user.password = make_password(user.password)
            user.save()
            print("user created")
            return redirect('/login')

    return render(request, "signup.html")
