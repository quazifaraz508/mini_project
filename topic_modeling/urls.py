from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_fun_topic_modeling, name = "main_fun_topic_modeling"),
]
