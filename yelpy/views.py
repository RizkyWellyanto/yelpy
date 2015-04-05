from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.context_processors import csrf

from models import Rating, UserProfile


def home(request):
    context = {}
    context['user'] = request.user
    context.update(csrf(request))

    return render(request, 'home.html', context)


def auth(request):
    context = {}
    context.update(csrf(request))
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username and password:
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)

                user_url = '/users/%s' % user.id
                return redirect(user_url)

    return redirect('/')


@login_required
def log_out(request):
    logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        # Catch duplicate usernames
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            pass
        else:
            return redirect('/')

        if username and password:
            user = User(
                username=username,
            )
            user.set_password(password)
            user.save()

            user_pro = UserProfile(
                user=user,
            )
            user_pro.save()

            user_url = '/users/%s' % user.id
            return redirect(user_url)

    return redirect('/')


@login_required
def user_view(request, user_id):
    viewed_user = User.objects.get(id=user_id)
    context = {}
    context.update(csrf(request))
    context['user'] = request.user
    context['viewed_user'] = viewed_user
    context['ratings'] = viewed_user.ratings.all()
    return render(request, 'user.html', context)


@login_required
def create_comment(request, user_id):
    for_user = User.objects.get(id=user_id)
    rater = request.user
    #stop user from rating them
    score = request.POST.get('score', None)
    review = request.POST.get('review', None)

    if score and review:
        rating = Rating(
            for_user=for_user,
            rater=rater,
            score=score,
            review=review
        )
        rating.save()

    user_url = '/users/%s' % user_id
    return redirect(user_url)

# This is the search for user method @Rizky
def search_user(request, user_id):
    target_user = request.searchName
