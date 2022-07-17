from django.db.models.signals import pre_save #Django Signals 
from django.dispatch import receiver
from .models import Question, Answer
from django.utils.text import slugify


@receiver(pre_save, sender=Question)
def add_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug
        