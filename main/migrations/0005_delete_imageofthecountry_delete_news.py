# Generated by Django 4.2.1 on 2023-05-18 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_date_created_imageofthecountry_created_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageOftheCountry',
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
