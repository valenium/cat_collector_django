# All paths specific to catcollector
from django.urls import path
# eventually pointing to view functionality which handles requests and responses
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Anticipate there to be a home function within views.py
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index'),
]

