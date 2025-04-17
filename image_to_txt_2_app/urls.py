from django.urls import path
from . import views


urlpatterns = [
    path('', views.image_to_txt_function , name = 'image_to_txt_func')    
]
