from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    description2 = models.TextField(blank=True, null=True, default=None)
    description3 = models.TextField(blank=True, null=True, default=None)
    slug = models.SlugField(max_length=300, unique=True)
    url = models.URLField(max_length=300)
    url2 = models.URLField(max_length=300)
    url3 = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    picture6 = CloudinaryField('image')
    picture1 = CloudinaryField('image')
    picture2 = CloudinaryField('image')
    picture3 = CloudinaryField('image')
    picture4 = models.ImageField(upload_to='images/',blank=True, null=True, default=None)
    picture5 = models.ImageField(upload_to='images/',blank=True, null=True, default=None)
    video = models.FileField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.title