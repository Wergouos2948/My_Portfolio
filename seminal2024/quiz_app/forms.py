from django.forms import ModelForm
from .models import Page

class UploadFileForm(ModelForm):
    class Meta:
        model = Page
        fields = ["source", "source_text", "quiz_text", "correct", "incorrect_1", "incorrect_2"]