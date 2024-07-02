from django.db import models

# Create your models here.

class MyModel(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    birth_date=models.DateField()
    schedule=models.DateTimeField()
    duration_field = models.DurationField()
    float_field = models.FloatField()
    cgpa=models.DecimalField(max_digits=5,decimal_places=5)
    careerpath=models.BooleanField()
    binary_field = models.BinaryField()
    big_integer_field = models.BigIntegerField()
    small_integer_field = models.SmallIntegerField()
    time_field = models.TimeField()