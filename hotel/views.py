from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
# Create your views here.
def home(request):
    rooms=Room.objects.filter(booked=False) [:3]
    context={'rooms': rooms}
    return render(request, 'index.html', context)


def room(request):
    all_rooms = Room.objects.filter(booked=False)
    context = {'all_rooms': all_rooms}
    return render(request, 'rooms.html', context)

def single_room(request,pk):
    post = Room.objects.get(pk=pk)
    context= {'post':post}
    return render(request,'roomdetails.html', context)


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	context = {"register_form": form}
	return render (request, 'register.html', context)

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	context = {"login_form": form}
	return render(request, "login.html", context)

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("home")
