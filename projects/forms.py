from django import forms
from .models import Projects,Ideas,Comments,Student

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['student']

class IdeaForm(forms.ModelForm):
    class Meta:
        model =Ideas
        exclude=['student']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude=['project']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude=['name']

