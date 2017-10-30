from django.forms import ModelForm,Field,Widget,PasswordInput,TextInput
from django.contrib.auth.models import User
# from django.utils.translation import ugettext_lazy as _
class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        help_texts={
            'username':None
        }
        widget ={
            'username':TextInput(attrs={'class':'form-control','name':'username',
                                        'id':'username','maxlength':256,'placeholder':'用户名'}),

        'password':PasswordInput(attrs={'class':'form-control','name':'password','id':'password',
                                        'maxlength':30,'placeholder':'密码'})
        }
