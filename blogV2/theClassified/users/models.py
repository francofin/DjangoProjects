from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.dispatch import receiver
# Create your models here.


class UserRoles(models.TextChoices):
     SUBSCRIBER = 'Subscriber'
     SELLER = 'Seller'
     ADMIN = 'Admin'
     EMPLOYEE = 'Employee'
     ROLE='Client'

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='userprofile', on_delete=models.CASCADE)
    store_name = models.CharField(max_length=300, blank=True, null=True, default=None)
    company_number = models.CharField(max_length=300, blank=True, null=True, default=None)
    company_email = models.EmailField(max_length=300, blank=True, null=True, default=None, validators=[EmailValidator()])
    address = models.CharField(max_length=700, null=True)
    about = models.TextField(blank=True, null=True, default=None)
    about1 = models.TextField(blank=True, null=True, default=None)
    about2 = models.TextField(blank=True, null=True, default=None)
    about3 = models.TextField(blank=True, null=True, default=None)
    about4 = models.TextField(blank=True, null=True, default=None)
    about5 = models.TextField(blank=True, null=True, default=None)
    about6 = models.TextField(blank=True, null=True, default=None)
    about7 = models.TextField(blank=True, null=True, default=None)
    about8 = models.TextField(blank=True, null=True, default=None)
    about9 = models.TextField(blank=True, null=True, default=None)
    about10 = models.TextField(blank=True, null=True, default=None)
    about11 = models.TextField(blank=True, null=True, default=None)
    about12 = models.TextField(blank=True, null=True, default=None)
    about13 = models.TextField(blank=True, null=True, default=None)
    about14 = models.TextField(blank=True, null=True, default=None)
    phone_number = models.CharField(max_length=300, blank=True, null=True, default=None)
    cover_picture = models.FileField(blank=True, null=True, default=None)
    profile_picture6 = CloudinaryField('profile_picture6', blank=True, null=True, default=None)
    profile_picture1 = CloudinaryField('profile_picture1', blank=True, null=True, default=None)
    profile_picture2 = CloudinaryField('profile_picture2', blank=True, null=True, default=None)
    profile_picture3 = CloudinaryField('profile_picture3', blank=True, null=True, default=None)
    profile_picture4 = CloudinaryField('profile_picture4', blank=True, null=True, default=None)
    profile_picture5 = CloudinaryField('profile_picture5', blank=True, null=True, default=None)
    profile_picture7 = models.FileField(blank=True, null=True, default=None)
    profile_picture8 = models.FileField(blank=True, null=True, default=None)
    profile_picture9 = CloudinaryField('profile_picture9', blank=True, null=True, default=None)
    profile_picture11 = CloudinaryField('profile_picture11', blank=True, null=True, default=None)
    profile_picture12 = models.FileField(blank=True, null=True, default=None)
    profile_picture10 = models.FileField(blank=True, null=True, default=None)
    date_of_birth = models.DateField(blank=True, null=True, default=None)
    resume = models.FileField(null=True, blank=True)
    document = models.FileField(null=True, blank=True)
    document1 = models.FileField(null=True, blank=True)
    document2 = models.FileField(null=True, blank=True)
    document3 = models.FileField(null=True, blank=True)
    document4 = models.FileField(null=True, blank=True)
    stripe_account_id = models.CharField(max_length=500, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.FileField(blank=True, null=True, default=None) 

    def __str__(self):
        return self.user.first_name


class CustomUser(AbstractUser):
    
    user_security_identifier = models.CharField(max_length=500, unique=True, default=None)
    role = models.CharField(max_length=300, choices=UserRoles.choices, default=UserRoles.SUBSCRIBER)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name