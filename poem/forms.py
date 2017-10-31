import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _

class LoginForm(forms.ModelForm):
    '''登录表单'''
    class Meta:
        model = User
        fields = ['username','password']
        help_texts={
            'username':None
        }
        labels={
            'username':'用户',
            'password':'密码'
        }
        widgets ={
            'username':forms.TextInput(
                attrs={'class':'form-control','name':'username',
                                        'id':'username','maxlength':256,
                                        'placeholder':'用户名'}),

        'password':forms.PasswordInput(
            attrs={'class':'form-control','name':'password','id':'password',
                                        'maxlength':30,'placeholder':'密码'})
        }

class PWDForm(forms.Form):
    '''修改密码的表单'''
    password = forms.CharField(label='密码',max_length=30,
                         widget=forms.PasswordInput(
                             attrs={'class':'form-control',
                                    'name':'password','placeholder':'请输入密码'}))
    repassword = forms.CharField(label='再次输入',max_length=30,
                                 widget=forms.PasswordInput(
                                     attrs={'class':'form-control',
                                            'name':'repassword',
                                            'placeholder':'再次输入密码'}))
    def clean_password(self):
        '''程序先运行clean_password() 再云信clean()'''
        password = self.cleaned_data['password'].strip()
        if len(password) < 5:
            raise ValidationError('密码太短')
        if len(password) > 15:
            raise ValidationError('密码太长')
        if password.isdigit():
            raise ValidationError('密码不能是纯数字')
        return password

    def clean(self):

        if self.cleaned_data.get('password') == self.cleaned_data.get('repassword').strip():
            return self.cleaned_data
        else:
            raise ValidationError('两次密码不一致')


