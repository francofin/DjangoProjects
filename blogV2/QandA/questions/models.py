from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
# Create your models here.


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

class Question(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500)
    body = models.TextField()
    category = models.CharField(max_length=50, choices=Category.choices, default=Category.Technology)
    slug = models.SlugField(max_length=500, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'questions')
    image1 = models.ImageField(upload_to='question_images/', verbose_name='Image', null=True, default=None, blank=True)
    image2 = models.ImageField(upload_to='question_images/', verbose_name='Image', null=True, default=None, blank=True)
    image3 = models.ImageField(upload_to='question_images/', verbose_name='Image', null=True, default=None, blank=True)


    def __str__(self):
        return self.title

class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name = 'answers')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'answers')
    image1 = models.ImageField(upload_to='question_images/', verbose_name='Image', null=True, default=None, blank=True)
    image2 = models.ImageField(upload_to='question_images/', verbose_name='Image', null=True, default=None, blank=True)
    image3 = models.ImageField(upload_to='question_images/', verbose_name='Image', null=True, default=None, blank=True)


    def __str__(self):
        return self.author.username


class LikePost(models.Model):
    liked_at = models.DateTimeField(auto_now_add=True)
    

# class Images(models.Model):
#     question = models.ForeignKey(Question, default=None, on_delete=models.CASCADE)
#     answer = models.ForeignKey(Answer, default=None, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(upload_to='question_images/',
#                               verbose_name='Image')