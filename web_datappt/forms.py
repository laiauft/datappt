from django import forms
from django.core import validators
from web_datappt.functions import validate_file_extension
import os

class FileForm(forms.Form):  
    file = forms.FileField(validators=[validate_file_extension])
