# Generated by Django 3.2.9 on 2021-11-21 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_site', '0003_imagefile_add_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagelabel',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='user',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='userimgae',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]