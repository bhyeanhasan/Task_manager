from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import auth, User
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'homepage.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'User not found')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken!!')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email taken!!')
            return redirect('register')
        if pass1 == pass2:
            User.objects.create_user(username=username, email=email, password=pass1)
            return redirect('login')

        messages.info(request, 'Can not create')

    return render(request, 'register.html')
