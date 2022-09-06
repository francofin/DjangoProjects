from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from cloudinary.models import CloudinaryField
# Create your models here.


class UserRoles(models.TextChoices):
     SUBSCRIBER = 'Subscriber'
     SELLER = 'Seller'
     ADMIN = 'Admin'


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(blank=True, null=True, default=None)
    about = models.TextField()
    store_name = models.CharField(max_length=300, blank=True, null=True, default=None)
    company_number = models.CharField(max_length=300, blank=True, null=True, default=None)
    company_email = models.EmailField(max_length=300, blank=True, null=True, default=None, validators=[EmailValidator()])
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
    user_security_identifier = models.CharField(max_length=500, unique=True)
    phone_number = models.CharField(max_length=300, blank=True, null=True, default=None)
    cover_picture = models.ImageField(upload_to='images/')
    profile_picture6 = CloudinaryField('image')
    profile_picture1 = CloudinaryField('image')
    profile_picture2 = CloudinaryField('image')
    profile_picture3 = CloudinaryField('image')
    profile_picture4 = CloudinaryField('image')
    profile_picture5 = CloudinaryField('image')
    profile_picture7 = models.ImageField(upload_to='images/',blank=True, null=True, default=None)
    profile_picture8 = models.ImageField(upload_to='images/',blank=True, null=True, default=None)
    profile_picture9 = models.ImageField(upload_to='images/',blank=True, null=True, default=None)
    profile_picture11 = models.ImageField(upload_to='images/',blank=True, null=True, default=None)
    profile_picture12 = models.ImageField(upload_to='images/',blank=True, null=True, default=None)
    profile_picture10 = models.ImageField(upload_to='images/',blank=True, null=True, default=None)
    date_of_birth = models.DateField(null=True)
    resume = models.FileField(null=True, blank=True)
    document = models.FileField(null=True, blank=True)
    document1 = models.FileField(null=True, blank=True)
    document2 = models.FileField(null=True, blank=True)
    document3 = models.FileField(null=True, blank=True)
    document4 = models.FileField(null=True, blank=True)
    role = models.CharField(max_length=300, choices=UserRoles.choices)
    stripe_account_id = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.first_name