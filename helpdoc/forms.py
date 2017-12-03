from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Main, Content,Issue

class MainForm(ModelForm):
    class Meta:
        model = Main
        fields = ['title','detail','image',]


class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'detail'] 

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['detail','rectify']                