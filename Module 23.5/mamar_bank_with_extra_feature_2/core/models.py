from django.db import models

# Create your models here.
class UserBank(models.Model):
    bank_name = models.CharField(max_length=150)
    is_bankrupt = models.BooleanField(default=False)
    
    def __str__(self):
        return self.bank_name