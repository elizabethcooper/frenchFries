from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse, JsonResponse
import json
from .models import User


def login(request):
    return render(request, 'index.html', {'message': ''})


def register(request):
    return render(request, 'register.html')


def welcome(request):
	username = request.GET.get('username', None)
	if User.objects.filter(user_name=username).exists():
		return render(request, 'welcome.html', {'username': username})
	else:
		return render(request, 'index.html', {'message': 'Username not valid'})


def register_new_user(request):
    username = request.POST.get("username")
    name = request.POST.get("name")
    email = request.POST.get("email")
    user = User.objects.create(name=name, user_name=username, email=email)
    return redirect('/fries/welcome?username=' + username)


def login_user(request, username=None):
    username = username if username is not None else request.POST.get(
        'username')
    if User.objects.filter(user_name=username).exists():
        return redirect('/fries/welcome?username=' + username)
    else:
        return render(request, 'index.html', {'message': 'Username not valid'})
