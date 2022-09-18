from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.dispatch import receiver
from store.models import Store
# Create your models here.


class UserRoles(models.TextChoices):
     SUBSCRIBER = 'Subscriber'
     SELLER = 'Seller'
     ADMIN = 'Admin'
     EMPLOYEE = 'Employee'
     CLIENT='Client'

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='userprofile', on_delete=models.CASCADE)
    # store = models.OneToOneField(Store, on_delete=models.CASCADE, blank=True, null=True, default=None)
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
    cover_picture = models.CharField(max_length=600, blank=True, null=True, default=None) 
    profile_picture6 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    profile_picture1 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    profile_picture2 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    profile_picture3 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    profile_picture4 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    profile_picture5 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    profile_picture7 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    profile_picture8 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    profile_picture9 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    profile_picture11 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    profile_picture12 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    profile_picture10 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    date_of_birth = models.DateField(blank=True, null=True, default=None)
    resume = models.CharField(max_length=600, blank=True, null=True, default=None) 
    document = models.CharField(max_length=600, blank=True, null=True, default=None) 
    document1 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    document2 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    document3 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    document4 = models.CharField(max_length=600, blank=True, null=True, default=None) 
    stripe_account_id = models.CharField(max_length=500, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.user.first_name


class CustomUser(AbstractUser):
    profile_picture = models.FileField(blank=True, null=True, default=None)
    profile_picture_cs = models.CharField(max_length=600, blank=True, null=True, default=None) 
    user_security_identifier = models.CharField(max_length=500, unique=True, default=None)
    role = models.CharField(max_length=300, choices=UserRoles.choices, default=UserRoles.SUBSCRIBER)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name