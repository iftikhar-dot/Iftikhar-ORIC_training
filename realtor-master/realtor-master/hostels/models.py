from django.db import models
from datetime import datetime
from owners.models import Owner


class NearbyUniversities(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Utilities(models.Model):
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name


class Hostel(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    location = models.TextField(default="")
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    nearby_universities = models.ManyToManyField(
        NearbyUniversities, null=True, blank=True
    )  # state
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    seater = models.IntegerField()  # bedrooms
    bathrooms = models.IntegerField()
    hostel_choices = (  # garage
        ("Boys Hostel", "Boys Hostel"),
        ("Girls Hostel", "Girls Hostel"),
    )
    hostel_type = models.CharField(
        max_length=100, choices=hostel_choices, default="Male"
    )

    available = models.BooleanField(default=True)
    utilities = models.ManyToManyField(Utilities, null=True, blank=True)
    photo_main = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_5 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_6 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
