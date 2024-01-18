
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import datetime
from .managers import CustomUserManager

class User(AbstractUser):
    username=None
    email = models.EmailField(unique = True,blank=False)
    date_created= models.DateTimeField(default=datetime.now(), blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()

    objects = CustomUserManager()
    def __str__(self):
        return "{}".format(self.email)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField( max_length=50,default='')
    email_token=models.CharField( max_length=100)
    is_verified=models.BooleanField(default=False)

