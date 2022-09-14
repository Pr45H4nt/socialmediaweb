from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')

class loginForm(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput())

class postform(forms.ModelForm):
    class Meta:
        model = post
        fields = ('status',)

class commentform(forms.ModelForm):
    class Meta:
        model = comments
        fields = ('comment',)

class replyform(forms.ModelForm):
    class Meta:
        model = replycomment
        fields = ('reply',)