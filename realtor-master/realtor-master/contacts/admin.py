from django.contrib import admin
from django.db import models
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "hostel", "email", "contact_date")
    list_display_links = ("id", "name")
    search_fields = ("name", "email", "hostel")
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
