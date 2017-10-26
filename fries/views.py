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
	return render(request, 'welcome.html')


def register_new_user(request):
	username = request.POST.get("username")
	name = request.POST.get("name")
	email = request.POST.get("email")
	user = User.objects.create(name=name, user_name=username, email=email)
	return HttpResponse(json.dumps(user.values()), content_type="application/json")

def login_user(request, username=None):
	username = username if username is None  else request.GET.get('username')
	if User.objects.filter(user_name=username).exists():
		return redirect('/fries/welcome')
	else:
		return render(request, 'index.html', {'message': 'Username not valid'})

