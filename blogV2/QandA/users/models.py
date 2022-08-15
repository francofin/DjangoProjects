from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='images/')
    about = models.TextField()
    date_of_birth = models.DateField(null=True)
    role = models.CharField(max_length=300)


    def __str__(self):
        return self.username