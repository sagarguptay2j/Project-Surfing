from .models import Usergroup
from django import forms

class UsergroupForm(forms.ModelForm):

    class Meta():
        model=Usergroup
        fields = ('name','description')
