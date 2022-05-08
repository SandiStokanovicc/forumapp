from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Learn python!', },
    {'id': 2, 'name': 'Learn frontend', },
    {'id': 3, 'name': 'Learn django', }
]


def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
