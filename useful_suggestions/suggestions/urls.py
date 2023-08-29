from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_suggestions/', views.create_suggestions, name='create_suggestions')
]