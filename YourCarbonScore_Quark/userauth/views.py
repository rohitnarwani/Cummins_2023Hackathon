from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Account
# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        data = request.POST
        email = data['email']
        password = data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Couldn't Login. Please check your credentials.")
    return render(request, 'userauth/login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        data = request.POST
        fullname = data['fullname']
        email = data['email']

        password = data['password']
        password2 = data['password2']
        if password == password2:
            if Account.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use. Please use another email.')
                return redirect('signup')
            else:
                user=Account.objects.create_user(fullname=fullname, email=email, password=password)
                user.save()
                login(request, user)
                messages.info(request, 'Account created successfully.')
                return redirect('home')
        else:
            messages.error(request, 'Please make sure the passwords match.')
            return redirect('signup')
    return render(request, 'userauth/signup.html')

def logout_user(request):
    if request.method == 'POST' and request.user.is_authenticated:
        logout(request)
        messages.info(request, 'You have been logged out.')
        return redirect('home')
    if not request.user.is_authenticated:
        return redirect('home')
    return redirect('home')