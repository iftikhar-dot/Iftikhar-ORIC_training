# Generated by Django 3.2.7 on 2021-09-29 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0006_auto_20210929_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='hire_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 9, 29, 16, 16, 39, 421834)),
        ),
    ]
