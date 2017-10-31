from django.forms import ModelForm,Field,Widget,PasswordInput,TextInput,EmailInput
from django import forms
from django.forms import fields
from django.forms import widgets
from django.contrib.auth.models import User
from poem import models
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

# from django.utils.translation import ugettext_lazy as _
class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        help_texts={
            'username':None
        }
        widgets ={
            'username':TextInput(attrs={'class':'form-control','name':'username',
                                        'id':'username','maxlength':256,'placeholder':'用户名'}),

        'password':PasswordInput(attrs={'class':'form-control','name':'password','id':'password',
                                        'maxlength':30,'placeholder':'密码'})
        }


class RegForm(ModelForm):
    repeat_password = fields.CharField(label='重新输入密码',error_messages=({'required':'密码不能为空'}),widget=forms.PasswordInput(attrs={'class':'form-control','name':'repeat_password','id':'id_repeat_password',
                                        'placeholder':'请重新输入密码'}))
    class Meta:
        model = User
        fields = ['username','email','password']
        help_texts={
            'username':None
        }
        labels={
            'username':'用户名',
            'password':'密码',
            'email':'邮箱',
            'repeat_password':'重新输入密码',
        }
        error_messages={
            'username':{
                'required':'用户名不能为空'
            },
            'email':{
                'required': '邮箱不能为空',
                'invalid': '邮箱格式错误..',
            },
            'password': {
                'required': '密码不能为空',
            },
        }
        widgets ={
            'username':widgets.TextInput(attrs={'class':'form-control','name':'username',
                                        'id':'id_username','maxlength':32,'placeholder':'用户名'}),

        'password':widgets.PasswordInput(attrs={'class':'form-control','name':'password','id':'id_password',
                                        'maxlength':30,'placeholder':'密码'}),
        'email':widgets.EmailInput(attrs={'class':'form-control','name':'email','id':'id_email',
                                        'maxlength':32,'placeholder':'邮箱'
                                        })
        }

    def clean(self):
        if self.cleaned_data.get('password') == self.cleaned_data.get('repeat_password'):
            return self.cleaned_data
        else:
            raise ValidationError('密码不一致')

    def clean_username(self):
        if self.cleaned_data.get('username').isdigit() or self.cleaned_data.get('username').isalpha():
            raise ValidationError('用户名必须是字母和数字的组合')
        elif User.objects.filter(username=self.cleaned_data.get('username')):
            raise ValidationError('用户名已存在')
        else:
            return self.cleaned_data['username']

    def clean_password(self):
        if len(self.cleaned_data.get('password'))>=4:
            return self.cleaned_data['password']
        else:
            raise ValidationError('密码不能小于4位')



