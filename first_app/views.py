from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import *
from first_app import forms


# Create your views here.
def index(request):
    diction = {'Title': 'This is Home Page!'}
    return render(request, 'first_app/index.html', context=diction)

def album_list(request):
    diction = {'Title': 'List of Albums'}
    return render(request, 'first_app/album_list.html', context=diction)

def musician_form(request):
    diction = {'Title': 'Add Musician'}
    return render(request, 'first_app/musicain_form.html', context=diction)

def album_form(request):
    diction = {'Title': 'Add Album'}
    return render(request, 'first_app/album_form.html', context=diction)

