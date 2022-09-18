from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Store
from django.utils.text import slugify 
from datetime import datetime
import uuid


@receiver(pre_save, sender = Store)
def add_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.name) + instance.id
        instance.slug = slug
        
@receiver(pre_save, sender = Store)
def add_security_id(sender, instance, *args, **kwargs):
    if instance and not instance.unique_identifier:
        unique_identifier = uuid.uuid5(uuid.NAMESPACE_DNS, (str(instance.name) + str(instance.id) +str(datetime.now())))
        instance.unique_identifier = unique_identifier

        return unique_identifier