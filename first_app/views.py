from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    diction = {'text_1':'I am from dictionary'}
    return render(request,'first_app/index.html',context=diction)

def contact(request):
    return HttpResponse("<h1>This is Contact<h1> <a href='/'>index</a><a href='/about/'>About</a>")

def about(request):
    return HttpResponse("<h1>This is About<h1> <a href='/'>index</a><a href='/contact/'>contact</a>")