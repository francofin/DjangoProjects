from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import CustomUser, UserProfile
import uuid
from datetime import datetime


@receiver(pre_save, sender = CustomUser)
def add_security_id(sender, instance, *args, **kwargs):
    if instance and not instance.user_security_identifier:
        user_security_identifier = uuid.uuid5(uuid.NAMESPACE_DNS, (str(instance.first_name) + str(instance.last_name)+str(instance.email) +str(datetime.now())))
        instance.user_security_identifier = user_security_identifier

        return user_security_identifier
        


@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, created, *args, **kwargs):
    
    print(instance)
    user = instance
    if created:
        profile = UserProfile(user=user)
        profile.save()