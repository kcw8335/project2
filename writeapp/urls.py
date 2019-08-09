from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.writeapp, name="writeapp"),
    path('writeuser/', views.writeuser, name="writeuser"),
]