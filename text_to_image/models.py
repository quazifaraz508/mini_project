from django.db import models
from django.utils import timezone

# Create your models here.


class image_to_txt_convert(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name