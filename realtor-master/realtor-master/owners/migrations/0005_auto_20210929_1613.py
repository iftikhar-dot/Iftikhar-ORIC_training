# Generated by Django 3.2.7 on 2021-09-29 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("owners", "0004_auto_20210929_1608"),
    ]

    operations = [
        migrations.AlterField(
            model_name="owner",
            name="hire_date",
            field=models.CharField(default="", max_length=10),
        ),
    ]
