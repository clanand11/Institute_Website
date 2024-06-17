from django.db import models
from django.contrib.auth.models import AbstractUser
from webapp.models import Course
from .manager import *

class CustomUser(AbstractUser):

    phone_num=models.CharField(max_length=20, unique=True)
    address= models.TextField()
    courses=models.ManyToManyField(Course,blank=True)

    REQUIRED_FIELDS=['phone_num']
    objects=UserManager()

# Create your models here.
