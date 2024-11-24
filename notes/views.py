from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

from notes.models import Note

@login_required()
def index(request):
    user = request.user

    notes = Note.objects.filter(owner=user)
    notes_list = [ { 'time' : note.time, 'body' : note.body, 'id' : note.id } for note in notes ]
    notes_list.sort(key=lambda note: note['time'])

    return render(request, 'index.html', { 'notes' : notes_list})


@login_required()
def add(request):
    if request.method == 'POST':
        user = request.user
        body = request.POST.get('body')

        Note.objects.create(owner=user, body=body)

    return redirect("index")


@login_required()
def remove(request, note_id):
    if request.method == 'POST':
        user = request.user
        note = Note.objects.get(pk=note_id)
        if user == note.owner:
            note.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'index'))


@login_required()
def search(request):
    if request.method == 'GET':
        user = request.user
        keyword = request.GET.get('keyword')

        notes = Note.objects.filter(owner=user, body__icontains=keyword)
        notes_list = [ { 'time' : note.time, 'body' : note.body, 'id' : note.id } for note in notes ]
        notes_list.sort(key=lambda note: note['time'])

        return render(request, 'search.html', { 'notes' : notes_list, 'keyword' : keyword})

    return redirect("index")


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, 'login.html', { 'login_failed' : True })

    return redirect("index")


def logout_view(request):
    if request.method == 'POST':
        logout(request)

    return redirect("index")
