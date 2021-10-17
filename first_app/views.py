from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import *

# Create your views here.
def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1':'This is a list of Musician','musician': musician_list}
    return render(request,'first_app/index.html',context=diction)

def contact(request):
    return HttpResponse("<h1>This is Contact<h1> <a href='/'>index</a><a href='/about/'>About</a>")

def about(request):
    return HttpResponse("<h1>This is About<h1> <a href='/'>index</a><a href='/contact/'>contact</a>")