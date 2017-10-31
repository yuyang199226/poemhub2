from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from . import forms



def log_in(request):
    '''登录'''
    if request.method == 'GET':
        loginform = forms.LoginForm()
        return render(request,'login.html',{'loginform':loginform})
    elif request.method == 'POST':
        loginform = forms.LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        #与数据库比对，判断用户名和密码输入是否正确
        user_obj = authenticate(request,username=username,password=password)
        #加入到session 中
        login(request,user_obj)
        if user_obj:
            return redirect('/home')
        else:
            context={'message':'用户名或者密码错误','loginform':loginform}
            return render(request,'login.html',context)



def signup(request):
    '''注册'''
    return HttpResponse('注册')

def log_out(request):
    '''注销'''
    return HttpResponse('注销')

def changepwd(request):
    '''修改密码'''
    if request.method == 'GET':
        pwd_form = forms.PWDForm()
        return render(request,'changepwd.html',{'pwd_form':pwd_form})
    elif request.method == 'POST':

        pwd_form = forms.PWDForm(request.POST)
        if pwd_form.is_valid():
            new_password = request.POST.get('password')
            request.user.set_password(new_password)
            request.user.save()
            return redirect('/login/')
        else:
            for field in pwd_form:
                if pwd_form.errors.get(field.name):
                    field.error_msg = pwd_form.errors.get(field.name)[0]
            return render(request,'changepwd.html',
                          {'pwd_form':pwd_form,'error_all':pwd_form.errors['__all__'][0]})

def home(request):
    return render(request,'home.html')

