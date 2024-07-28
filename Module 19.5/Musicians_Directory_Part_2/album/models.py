from django.db import models
from musician.models import MusicianModel
# Create your models here.

class AlbumModel(models.Model):
    album_name = models.CharField(max_length=255)
    release_date = models.DateField(auto_now_add=True)
    rating_CHOICES = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]
    rating = models.CharField(max_length=1,choices=rating_CHOICES)
    # Relations
    musicians = models.ForeignKey(MusicianModel,related_name='albums',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.album_name