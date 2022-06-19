# notification/views.py
from django.shortcuts import render

# for simple chat
def index(request):
   print('hi')
   return render(request, 'notification/index.html', {})

def room(request, room_name):
    return render(request, 'notification/room.html', {
        'room_name': room_name
    })