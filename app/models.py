import random

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        user = self.model(
                username=username,
                **kwargs,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **kwargs):
        user = self.create_user(
                username=username,
                password=password,
                **kwargs,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    date_of_birth = models.DateField(null=True)
    random_num = models.IntegerField(null=False)

    objects = MyUserManager()

    REQUIRED_FIELDS = []


@receiver(pre_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    if instance.random_num is None:
        instance.random_num = random.randint(0, 100)
