from django.conf.urls import url
from django.contrib import admin

from main import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^verify/', views.verify),
    url(r'^about/', views.about),
]
