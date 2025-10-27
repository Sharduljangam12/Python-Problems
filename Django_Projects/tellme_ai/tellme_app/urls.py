from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('hello/', views.hello, name='hello'),
]
