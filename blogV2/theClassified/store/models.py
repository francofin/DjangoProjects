from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
import geocoder
import os
from dotenv import load_dotenv
# Create your models here.

load_dotenv()

class Country(models.TextChoices):
    Canada='Canada'
    US = 'US'

class Category(models.TextChoices):
    Technology = 'Technology'
    Finance = 'Finance'
    Household = 'Household'
    Music = 'Music'
    Sales = 'Sales'
    Education = 'Education/Training'
    Mathematics = 'Mathematics'
    Physics = 'Physics'
    Retail = 'Retail'
    Others = 'Others'

class Product(models.Model):
    name = models.CharField(max_length=300, null=False)
    price = models.FloatField()
    description = models.TextField()
    description2 = models.TextField(blank=True, null=True, default=None)
    description2 = models.TextField(blank=True, null=True, default=None)
    picture1 = models.CharField(max_length=600, blank=True, null=True, default=None)
    picture2 = models.CharField(max_length=600, blank=True, null=True, default=None)
    picture3 = models.CharField(max_length=600, blank=True, null=True, default=None)
    picture4 = models.CharField(max_length=600, blank=True, null=True, default=None)
    picture5 = models.CharField(max_length=600, blank=True, null=True, default=None)
    picture6 = models.CharField(max_length=600, blank=True, null=True, default=None)
    picture7 = models.CharField(max_length=600, blank=True, null=True, default=None)
    count = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    unique_identifier = models.CharField(max_length=300)



class Store(models.Model):
    name = models.CharField(max_length=300, null=False)
    about = models.TextField(blank=True, null=True, default=None)
    description2 = models.TextField(blank=True, null=True, default=None)
    description3 = models.TextField(blank=True, null=True, default=None)
    picture1 = models.CharField(max_length=600, blank=True, null=True, default=None)
    picture2 = models.CharField(max_length=600, blank=True, null=True, default=None)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='store')
    products = models.ManyToManyField(Product, blank=True)
    employees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='store_employee')
    slug = models.SlugField(max_length=300, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=300)
    unique_identifier = models.CharField(max_length=300)
    address = models.CharField(max_length=700, null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=60, choices = Country.choices, default=Country.Canada)
    point = gismodels.PointField(default=Point(0.0, 0.0))


    def save(self, *args, **kwargs):
        # overrides the .save() function to add the coordinates before saving the Job.
        g = geocoder.mapquest(self.address, key=os.environ.get('GEOCODER_API'))
        print(g)
        lng = g.lng
        lat = g.lat

        self.point = Point(lng, lat)
        super(Store, self).save(*args, **kwargs)