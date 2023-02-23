from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from app.models import Songs

# from app.models import Songs, Resume


class SongCreationForm(ModelForm):
    class Meta:
        model = Songs
        fields = ['name', 'category', 'image', 'file']


# class ResumeForm(forms.ModelForm):
#    class Meta:
#       model = Resume
#       fields = ['email','name','file']


class RegistrationForm(UserCreationForm):

    username = forms.CharField(help_text='')
    password1 = forms.CharField(help_text='', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
