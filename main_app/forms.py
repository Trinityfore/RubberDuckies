from dataclasses import field
from django.forms import ModelForm
from .models import Display

class DisplayForm(ModelForm):
    class Meta:
        model = Display
        fields = ('from_date','to_date', 'location')