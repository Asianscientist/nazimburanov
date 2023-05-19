# Generated by Django 4.2.1 on 2023-05-18 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageofthecountry',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 19, 11, 10, 842221)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='videomodel',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
