from django.db import models

# Create your models here.
from django.db import models

class UserRegistration(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

class Meta:
        db_table = 'EduTrack_userregistration' 
