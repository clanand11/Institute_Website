from django.shortcuts import render, redirect
from  django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *

def userLogin(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homePage')
        else:
            messages.success(request,("There was an error !! "))
            return redirect('loginpage')
    else:
        return render(request, 'members/login.html', {})
    
def userLogout(request):
    logout(request)
    messages.success(request,("Successfully Logged Out !! "))
    return redirect('homePage')

def userRegister(request):
    if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'Successfully Registered')
            return redirect('homePage')
    else:
        form=RegisterForm()

    return render(request, 'members/register.html',{'form':form})

def allusers(request):
    if request.user.is_superuser:
        users=CustomUser.objects.all()
        return render(request, 'members/allusers.html',{'users':users})

def deleteUser(request,user_id):
    if request.user.is_superuser:
        user=CustomUser.objects.get(pk=user_id)
        user.delete()
        messages.success(request, "User Deleted !!")
        return redirect('allusersPage')

    

