from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import *
from first_app import forms

# Create your views here.
def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1':'This is a list of Musician','musician': musician_list}
    return render(request,'first_app/index.html',context=diction)

def form(request):
    new_form = forms.user_form()
    diction = {'test_form' : new_form,
               'heading1': "This form is created by django"}
    if request.method == 'post':
        new_form = forms.user_form(request.POST)
        if new_form.is_valid():
            diction.update({'field': new_form.cleaned_data['field']})
            diction.update({'form': "Yes"})

    return render(request,'first_app/form.html',context=diction)