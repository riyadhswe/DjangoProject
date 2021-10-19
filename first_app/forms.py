from django import forms
from django.core import validators

class user_form(forms.Form):
    name = forms.CharField()
