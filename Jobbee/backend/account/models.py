from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    # related name helps maintain the relationship with the user model. 
    # One to One maintainse the relationship with the user model.
    resume = models.FileField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)