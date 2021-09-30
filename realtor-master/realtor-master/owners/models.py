from django.db import models
from datetime import datetime

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Owner(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=CASCADE, null=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(datetime.now())
