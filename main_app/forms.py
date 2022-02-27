from dataclasses import field
from msilib.schema import Class
from django.forms import ModelForm
from .models import Display

class DisplayForm(ModelForm):
    class Meta:
        model = Display
        fields = ('date', 'location')