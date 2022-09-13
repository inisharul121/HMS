from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import CreateView

from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
import operator

from .forms import NewUserForm, BookingForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    rooms = Room.objects.filter(booked=False)[:3]
    context = {'rooms': rooms}
    return render(request, 'index.html', context)


def room(request):
    all_rooms = Room.objects.filter(booked=False)
    context = {'all_rooms': all_rooms}
    return render(request, 'rooms.html', context)


def single_room(request, pk):
    post = Room.objects.get(pk=pk)
    context = {'post': post}
    return render(request, 'roomdetails.html', context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    context = {"register_form": form}
    return render(request, 'register.html', context)


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
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "login.html", context)


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")


'''def createBooking(request):
    if request.user.is_authenticated:
        #room = Room.objects.get(id=pk)
        #book=Booking.objects.get(id=pk)
        #print(room)
        #BookingFormSet = inlineformset_factory(User, Booking,fields=('Name', 'email', 'address_type', 'phone', 'room', 'user','endtime',), extra=10)
        #guest = User.objects.get(id=pk)
        #print(guest)
        #formset = BookingFormSet(queryset=Booking.objects.none(), instance=guest)
        # form = OrderForm(initial={'customer':customer})
        if request.method == 'POST':
            # print('Printing POST:', request.POST)
            # form = OrderForm(request.POST)
            #formset = BookingFormSet(request.POST, instance=guest)
            #if formset.is_valid():
             #   formset.save()


            return redirect('/')

        room.booked = True

        context = {'form': formset}
        return render(request, 'booking.html', context) '''


class CreateBooking(CreateView):
    model = Booking
    template_name = 'booknow.html'
    form_class = BookingForm

    @transaction.atomic
    def form_valid(self, form):
        # check user auth or create
        print(form.cleaned_data['room'])
        if self.request.user.is_authenticated:
            user = self.request.user
        else:
            user = User.objects.filter(username=form.cleaned_data['phone']).first()
            if not user:
                user = User.objects.create(

                )
        post = form.save(commit=False)
        post.user = user
        post.complete = True
        post.save()
        room = form.cleaned_data['room']
        room.booked = True
        #room.id = self.object.pk
        room.save()
        return redirect('profile')


@login_required
def Profile(request):
    user = request.user
    print(user)
    booked = Booking.objects.filter(user=request.user).order_by('-id')[:1]
    print(booked)
    context = {'booked': booked, 'user': user}
    return render(request, 'User.html', context)


@user_passes_test(operator.attrgetter('is_staff'))  # is_staff= superuser
def AdminDashboard(request):
    booked = Room.objects.filter(booked=True)
    bookedcount = Room.objects.filter(booked=True).count()
    unbooked = Room.objects.filter(booked=False)
    unbookedcount = Room.objects.filter(booked=False).count()
    context = {'booked': booked, 'unbooked': unbooked, 'bookedcount': bookedcount, 'unbookedcount': unbookedcount }

    return render(request, 'admindashboard.html', context)
