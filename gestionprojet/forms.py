from django.forms import ModelForm
from django.forms.models import fields_for_model
from .models import *
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name','descrp']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name','descr']