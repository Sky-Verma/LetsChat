from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from .models import  User_Info
from django.contrib import messages
from django.contrib.auth.models import User
from . import forms

# Create your views here.

def index(request):
    return render(request,'LC/index.html')

def login_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('loginForm'))
    return HttpResponseRedirect(reverse('my_profile'))

def login_request(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request,'LC/login.html',{
                'message':'Invalid Credentials.'
                
            })
    return render(request,'LC/login.html')

def signup_view(request):
    form=forms.CustomUserCreateForm()
    if request.method=='POST':
        form=forms.CustomUserCreateForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password1']
            form.save()
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
            return HttpResponseRedirect(reverse('my_profile'))
        else:
            if not form.is_valid():
                context={'form':form,'message':'Not valid.'}
            return render(request,'LC/signup.html',context)
    return render(request,'LC/signup.html',{'form':form})

def my_profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    form=forms.updateForm(instance=request.user.user_info)
    if request.method=="POST":
        form=forms.updateForm(request.POST,request.FILES,instance=request.user.user_info)
        if form.is_valid():
            form.save()
    return render(request,'LC/my_profile.html',{'form':form})

def users(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    users=User.objects.all()
    return render(request,'LC/users.html',{'users':users})

def chats(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request,'LC/chats.html')

def logout_view(request):
    logout(request)
    return render(request,'LC/login.html',{'message':'Logged Out.'})