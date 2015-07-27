__author__ = 'anjaneyulubatta'
from .models import FileUpload
from django import forms
class FileUploadModelForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['File']
