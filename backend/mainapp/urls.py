from django.contrib import admin
from django.urls import path, include
from mainapp.views import *

urlpatterns = [
    path('get_answer/', get_answer),
    path('get_user/',get_user),
    path('day_card/',day_card),
]
