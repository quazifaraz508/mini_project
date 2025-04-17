from django.urls import path
from . import views


urlpatterns = [
    path('', views.ner_logic, name= 'ner_logic')
]
