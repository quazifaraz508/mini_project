from django.urls import path
from . import views

urlpatterns = [
    path('', views.encoder_view, name= 'encoder_view') 
]
