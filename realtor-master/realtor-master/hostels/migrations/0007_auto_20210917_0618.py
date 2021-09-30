# Generated by Django 2.2.13 on 2021-09-17 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hostels", "0006_auto_20210917_0458"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hostel",
            name="Food_facility",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")], default="Yes", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="hostel",
            name="For",
            field=models.CharField(
                choices=[
                    ("Boys Hostel", "Boys Hostel"),
                    ("Girls Hostel", "Girls Hostel"),
                ],
                default="Male",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="hostel",
            name="laundary_facility",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")], default="Yes", max_length=100
            ),
        ),
    ]
