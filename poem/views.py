from django.shortcuts import render,redirect,HttpResponse
from . import forms
import copy


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
    if request.method == "GET":
        regform = forms.RegForm()
        return render(request,'reg.html',{'regform':regform})
    elif request.method == "POST":
        regform = forms.RegForm(request.POST)
        error_all_ = ''
        if regform.is_valid():
            regform.save()
            return redirect('/login/')
        else:
            if regform.errors.get('__all__'):
                error_all_ = regform.errors.get('__all__')[0]
            return render(request, 'reg.html', {'regform':regform,'error_all_':error_all_})

def log_out(request):
    '''注销'''
    return HttpResponse('注销')

def home(request):
    return HttpResponse('home web')



