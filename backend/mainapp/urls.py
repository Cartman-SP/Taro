from django.contrib import admin
from django.urls import path, include
from mainapp.views import *

urlpatterns = [
    path('get_answer/', get_answer),
    
]
