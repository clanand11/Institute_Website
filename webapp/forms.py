from django import forms
from django.forms import ModelForm 
from .models import *


class CourseForm(ModelForm):
    name=forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class':'form-control'}))
    fees=forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class':'form-control'}))
    duration=forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=Course
        fields="__all__"
        # labels={
        #     'name': 'Name',
        #     'description': 'Description',
        # }
        widgets={
            'description': forms.Textarea(attrs={'class' :'form-control' }),
        }