from django import forms
from django.core import validators
from first_app import models


class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        #fields = ('first_name','last_name')
        #exclude = ['first_name']   for remove
        fields = "__all__"
