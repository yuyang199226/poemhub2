from django.shortcuts import render,redirect,HttpResponse
from . import forms


def log_in(request):
    '''登录'''
    if request.method == 'GET':
        loginform = forms.LoginForm()
        return render(request,'login.html',{'loginform':loginform})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        return redirect('/home')


def signup(request):
    '''注册'''
    return HttpResponse('注册')

def log_out(request):
    '''注销'''
    return HttpResponse('注销')

def home(request):
    return HttpResponse('home web')

