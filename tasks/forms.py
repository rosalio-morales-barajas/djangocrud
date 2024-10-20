from django.forms import ModelForm
from .models import Tasks
from django import forms


class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert a title, please'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Insert a description, please'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input, m-auto'}),
        }
   
