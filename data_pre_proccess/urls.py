from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_pre_processing, name='data_pre_processing')
]
