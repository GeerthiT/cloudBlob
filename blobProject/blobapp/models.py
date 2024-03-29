from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# models.py


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

