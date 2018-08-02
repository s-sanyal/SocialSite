from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mail=models.CharField(max_length=100)
    work=models.CharField(max_length=150)
    residence=models.CharField(max_length=50)

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance, created, **kwargs):
         if created:
             Profile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
         instance.profile.save()

    def __str__(self):
        return str(self.user.username)
    



