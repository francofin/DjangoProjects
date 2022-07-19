from datetime import timedelta
from datetime import *
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
import geocoder
import os
from dotenv import load_dotenv
# Create your models here.

load_dotenv()

class JobType(models.TextChoices):
    Permanent = 'Permanent'
    Temporary = 'Contract'
    Internship = 'Internship'
    Volunteer = 'Volunteer'

class Education(models.TextChoices):
    Bachelors = 'Bachelors'
    Masters = 'Masters'
    Phd = 'Phd'
    Certificate = 'Certificate'

class Industry(models.TextChoices):
    Business = 'Business'
    IT = 'Information Technology'
    Banking = 'Banking'
    Marketing = 'Marketing'
    Energy = 'Energy'
    Sales = 'Sales'
    Education = 'Education/Training'
    Telecommunication = 'Telecommunication'
    Retail = 'Retail'
    Others = 'Others'

class Experience(models.TextChoices):
    NO_EXPERIENCE = 'No Experience'
    ONE_YEAR = '1 Years'
    TWO_YEAR = '2 Years'
    THREE_YEAR_PLUS = '3 Years above'

def return_date_time():
    now = datetime.now()
    return now + timedelta(days=20)

class Job(models.Model):
    title = models.CharField(max_length=200, null=True)
    section_one = models.TextField(null=True)
    section_two = models.TextField(null=True)
    section_three = models.TextField(null=True, blank=True)
    section_four = models.TextField(null=True, blank=True)
    section_five = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, validators=[EmailValidator()])
    address = models.CharField(max_length=700, null=True)
    jobType = models.CharField(max_length=50, choices=JobType.choices, default=JobType.Permanent)
    education = models.CharField(max_length=50, choices=Education.choices, default=Education.Bachelors)
    industry_detail = models.TextField(null=True)
    industry = models.CharField(max_length=50, choices=Industry.choices, default=Industry.Business)
    education_detail = models.TextField(null=True)
    experience = models.CharField(max_length=50, choices=Experience.choices, default=Experience.NO_EXPERIENCE)
    salary = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(10000000)])
    positions = models.IntegerField(default=1)
    company = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100, default="none")
    point = gismodels.PointField(default=Point(0.0, 0.0))
    applicationExpiry = models.DateTimeField(default = return_date_time)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # If user who created job is deleted, the user is set to null.
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        # overrides the .save() function to add the coordinates before saving the Job.
        g = geocoder.mapquest(self.address, key=os.environ.get('GEOCODER_API'))
        print(g)
        lng = g.lng
        lat = g.lat

        self.point = Point(lng, lat)
        super(Job, self).save(*args, **kwargs)



class CandidatesApplied(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    resume = models.CharField(max_length=200)
    applied_at = models.DateTimeField(auto_now_add=True)
    