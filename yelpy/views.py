from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.context_processors import csrf

def home(request):
    context = {}
    context['user'] = request.user
    context.update(csrf(request))
    return render(request, 'home.html', context)

def auth(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    context = {}
    context.update(csrf(request))
    if username and password:
        context['user'] = authenticate(username=username, password=password)

    return render(request, 'home.html', context)


def user_view(request, user_id):
    context = {}
    context['user'] = user_id
    return render(request, 'user.html', context)
