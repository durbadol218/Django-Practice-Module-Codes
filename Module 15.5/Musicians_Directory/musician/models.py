from django.db import models
# Create your models here.

class MusicianModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    instrument_type = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"