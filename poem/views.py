from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import copy
from .models import Profile
import json




def log_in(request):
    '''登录'''
    if request.method == 'GET':
        loginform = forms.LoginForm()
        return render(request,'login.html',{'loginform':loginform})
    elif request.method == 'POST':
        loginform = forms.LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        on = request.POST.get('remember')
        #与数据库比对，判断用户名和密码输入是否正确
        user_obj = authenticate(request,username=username,password=password)
        #加入到session 中
        if user_obj:
            if on:
                login(request, user_obj)
            return redirect('/home')
        else:
            context={'message':'用户名或者密码错误','loginform':loginform}
            return render(request,'login.html',context)

def signup(request):
    '''注册'''
    if request.method == "GET":
        regform = forms.RegForm()
        return render(request,'reg.html',{'regform':regform})
    elif request.method == "POST":
        regform = forms.RegForm(request.POST)
        error_all_ = ''
        if regform.is_valid():
            data = regform.cleaned_data
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            user_obj=User.objects.create_user(username=username,password=password,email=email)
            Profile.objects.create(user=user_obj,nickname=user_obj.username)
            return redirect('/login/')
        else:
            if regform.errors.get('__all__'):
                error_all_ = regform.errors.get('__all__')[0]
            return render(request, 'reg.html', {'regform':regform,'error_all_':error_all_})

def log_out(request):
    '''注销'''
    logout(request)


    return redirect('/home/')

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

@login_required
def user_profile(request):
    '''查看个人档案'''
    user = request.user.__str__()
    profile_obj = Profile.objects.filter(user__username=user).first()


    return render(request, 'user_profile.html', {'obj':profile_obj})

@login_required
def modify_profile(request):
    '''修改个人档案'''
    user = request.user.__str__()
    profile_obj = Profile.objects.filter(user__username=user).first()

    if request.method == 'POST':

        file_obj = request.FILES.get('avatar')
        nickname = request.POST.get('user')
        gender = request.POST.get('gender')
        person_bio = request.POST.get('person_bio')
        email = request.POST.get('email')

        if file_obj and file_obj != profile_obj.avator:
            profile_obj.avator = file_obj
        if nickname and nickname != profile_obj.nickname:
            profile_obj.nickname = nickname
        if gender and gender != profile_obj.gender:
            profile_obj.gender = gender
        if person_bio and person_bio != profile_obj.bio:
            profile_obj.bio = person_bio

        profile_obj.save()

        if email and email != profile_obj.user.email:
            User.objects.filter(username=user).update(email=email)
        return redirect('/home/')

    return render(request,'modify_profile.html',{'obj':profile_obj})

@login_required
def ajax_get_user_info(request):
    '''
    修改个人信息时获取修改信息的初始值
    :param request:
    :return:
    '''
    if request.method == 'GET':
        user = request.user.__str__()
        profile_obj = Profile.objects.filter(user__username=user).values('nickname','user__email','bio','gender')
        data = list(profile_obj)

        return HttpResponse(json.dumps(data))


    else:
        return HttpResponse('404，您要的网页已走丢。。。请重试')


