# -*- coding: utf-8 -*-
from django import forms
from imgComment.models import *

class UploadFileForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        file = self.cleaned_data["file"]
        if not file.name.endswith(".png") and not file.name.endswith(".jpg"):
            raise forms.ValidationError("The uploaded file is not an image file. "+file.name)
        return file








