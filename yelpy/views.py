from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    context = {}
    context['name'] = 'Jon Snow'
    return render(request, 'home.html', context)

def user_view(request, user_id):
    context = {}
    context['user'] = user_id
    return render(request, 'user.html', context)
