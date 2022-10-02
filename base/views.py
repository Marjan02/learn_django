from django.http import HttpResponse
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Room  # import Room class from models
from .forms import RoomForm

# Create your views here.

# rooms = [
#     {"id": 1, "name": "Let's learn Python!"},
#     {"id": 2, "name": "Let's learn Javascript!"},
#     {"id": 3, "name": "Design with me!"}
# ] # kita tidak membutuhkan ini lagi karna udah ada database


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}  # manggil variable
    return render(request, 'base/home.html', context)
    # return render(request, 'home.html', {'rooms': rooms}) #bisa juga gini


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})
