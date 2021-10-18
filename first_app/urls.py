from django.conf.urls import url
from django.urls import path
from first_app import views


urlpatterns = [
    path('', views.index,name="index"),
    path('contact/', views.contact,name="contact"),
    path('about/', views.about,name="about"),
    path('form/', views.form,name="form"),
]
