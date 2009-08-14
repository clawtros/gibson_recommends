from django import forms
from models import Place
from tagging.fields import TagField
from datetime import datetime


class PlaceForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea())
    class Meta:
        exclude = ('lng','lat','time_updated')
        model = Place
