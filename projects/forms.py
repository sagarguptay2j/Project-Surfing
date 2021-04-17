from .models import Project,Comment
from django import forms

class ProjectForm(forms.ModelForm):

    class Meta():
        model=Project
        fields = ('name','description','group')



class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('text',)
