from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class ClientUser(AbstractUser):
    age=models.PositiveIntegerField(null=True, blank=True)
    manzil=models.CharField(max_length=200)

