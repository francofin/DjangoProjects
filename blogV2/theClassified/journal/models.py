from random import choices
from django.db import models
from django.conf import settings
# Create your models here.

class JournalTypes(models.TextChoices):
     QUANTITATIVE = 'Quant'
     QUALITATIVE = 'Qualitative'
     RISK = 'Risk'
     CRYPTO = 'Crypto'
     BONDS='Fixed'
     DATASCIENCE='Data Science'
     PROGRAMMING='Programming'
     CODING ='Coding'
     PYTHON='Python'
     TRADING='Trading'
     MACRO='Macro Economic'

class Journal(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    file = models.FileField(blank=True, null=True, default=None)
    
    category = models.CharField(max_length=100, choices=JournalTypes.choices, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=300, default=None)
    url = models.URLField(max_length=300, blank=True, default=None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    author = models.TextField()
    image = models.URLField(max_length=400, null=True, default=None, blank=True)

    def __str__(self):
        return self.title
