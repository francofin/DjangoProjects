from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

# one to one use models.OneToOneField(model, on_delete, primary_key=True)
# many to many we use models.ManyToManyField(model)


class Publication(models.Model):
    title = models.CharField(max_length=50)


class Article(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #Foreign key to create many to one relationships, cascade, remove author, rmeoves all articles
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # publications = models.ManyToManyField(Publication)



    def __str__(self):
        return self.title