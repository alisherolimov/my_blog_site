from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


def index_view(request):
    context = {
        'banner': Banner.objects.all().order_by('-id')[:3],
        'phone': Phone.objects.last(),
        'more': More.objects.all().order_by('-id')[1:3],
        'mores': More.objects.last(),
        'course': Course.objects.all().order_by('-id')[:3],
        'discount': Discount.objects.last(),
        'services': Our_services.objects.all().order_by('-id')[:6],
        'thought': Thought.objects.all(),
        'upcoming_events': Upcoming_events.objects.all().order_by('-id')[:3]
    }
    return render(request, 'index.html', context)


def course_view(request):
    context = {
        'courses': Course.objects.all(),
        'phone': Phone.objects.last(),
        'banner': Banner.objects.last(),
    }
    return render(request, 'courses.html', context)


def elements_view(request):
    context = {
        'phone': Phone.objects.last(),
        'banner': Banner.objects.all().order_by('-id')[1],
        'services': Our_services.objects.all(),
    }
    return render(request, 'elements.html', context)


def news_view(request):
    context = {
        'phone': Phone.objects.last(),
        'banner': Banner.objects.last(),
        'news': News.objects.all().order_by('id')[:3],
        'new': News.objects.all().order_by('id')[3:6],
    }
    return render(request, 'news.html', context)


def contact_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )
        return redirect('contact_url')
    context = {
        'phone': Phone.objects.last(),
        'banner': Banner.objects.all().order_by('-id')[2],
    }
    return render(request, 'contact.html', context)


def new_post_view(request, pk):
    new = News.objects.get(pk=pk)
    context = {
        'new': new,
        'phone': Phone.objects.last(),
        'banner': Banner.objects.last(),
        'comment': Comment.objects.all()
    }
    return render(request, 'news_post.html', context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request,usr)
            return redirect('index_url')
    return render(request, 'log-in.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(
            username=username,
            password=password,
        )
        return redirect('index_url')
    return render(request, 'log-up.html')


def logout_view(request):
    logout(request)
    return redirect('signup_url')


def profile_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)


def delete_user_view(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('signup_url')


def create_comment_view(request, pk):
    new = News.objects.get(pk=pk)
    if request.method == 'POST':
        text = request.POST['text']
        Comment.objects.create(
            user=request.user,
            new=new,
            text=text,
        )
        return redirect('new_post_url', new.pk)
    return render(request, 'new_post.html', new.pk)


def edit_user_view(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('email')
        img = request.FILES.get('img')
        bio = request.POST.get('bio')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        user.username = username
        user.email = email
        user.bio = bio
        if img is not None:
            user.photo = img
        if new_password is not None:
            if new_password == confirm_password:
                user.set_password(new_password)

        user.save()
        return redirect('profile_url', user.pk)
    context = {
        'user': user
    }
    return render(request, 'edit-user.html', context)