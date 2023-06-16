from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email is already taken.')
            return redirect('home')

        user = User.objects.create_user(username=email, password=password)
        user.save()

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Failed to create user.')
            return redirect('home')

    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('signin') 
        else:
            messages.error(request, 'User not found or invalid credentials.')
            return redirect('home')

    return render(request, 'signin.html')

