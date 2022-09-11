from django.shortcuts import render,HttpResponse
from .models import *

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
