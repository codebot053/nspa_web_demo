from dataclasses import field
from django import forms
from .models import Project, DevTechnology


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title_image','technology_tag','title','content','location']