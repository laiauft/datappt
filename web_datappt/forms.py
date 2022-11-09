from django import forms
import os

class FileForm(forms.Form):  
    file = forms.FileField()

    def filename(self):
        return os.path.basename(self.file.name)