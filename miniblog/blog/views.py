from django.shortcuts import render, HttpResponseRedirect
from .forms import User_RegistrationFom, User_Authentication
from django.contrib.auth import authenticate, login, logout
from .models import User_Contact, Post

# Create your views here.


def home(request):
    post_data = Post.objects.all()
    return render(request, 'blog/home.html', {'post_data': post_data})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    if request.method == 'POST':
        un = request.POST.get('name')
        em = request.POST.get('email')
        address = request.POST.get('address')
        msg = request.POST.get('message')
        data = User_Contact(name=un, email=em, address=address, message=msg)
        data.save()
    return render(request, 'blog/contact.html')


def dashboard(request):
    post_data = Post.objects.all()
    if request.method == 'GET':
        st = request.GET.get('search')
        if st != None:
            post_data = Post.objects.filter(title__icontains=st)
    return render(request, 'blog/dashboard.html', {'post_data': post_data})


def addpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        des = request.POST.get('description')
        data = Post(title=title, description=des)
        data.save()
    return render(request, 'blog/addpost.html')


def user_signup(request):
    if request.method == 'POST':
        fm = User_RegistrationFom(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = User_RegistrationFom()
    return render(request, 'blog/signup.html', {'form': fm})


def user_login(request):
    if request.method == 'POST':
        fm = User_Authentication(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
    else:
        fm = User_Authentication()
    return render(request, 'blog/loginpage.html', {'form': fm})


def user_logout(request):
    pass
