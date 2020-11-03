from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class User_Info(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    about = models.TextField(null=True, max_length=1000)
    profile_pic = models.ImageField(
        default='defaultUser.png', null=True, blank=True)


def create_info(sender, **kwargs):
    if kwargs['created']:
        user_info = User_Info.objects.create(user=kwargs['instance'])


post_save.connect(create_info, sender=User)
