# Generated by Django 2.2.13 on 2021-09-17 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hostels", "0008_auto_20210917_0623"),
    ]

    operations = [
        migrations.RenameField(
            model_name="hostel",
            old_name="Food_facility",
            new_name="food_facility",
        ),
    ]