from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import NullBooleanField
from hostels.models import Hostel
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=CASCADE)
    gender = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)
    hostel = models.ForeignKey(Hostel, on_delete=DO_NOTHING, null=True)
