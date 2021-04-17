from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models

class UserCreateForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('college','gender','age','description')
