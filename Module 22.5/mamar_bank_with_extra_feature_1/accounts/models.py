from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE, GENDER
# django amaderke builtin user make korar facility dey!

class UserBankAccount(models.Model):
    user = models.OneToOneField(User, related_name='account',on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50,choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50,choices=GENDER)
    initial_deposite_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    
    def __str__(self):
        return str(self.account_no)  
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address',on_delete=models.CASCADE)
    street_address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.user.email) 