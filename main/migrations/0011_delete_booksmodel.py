# Generated by Django 4.1 on 2023-05-20 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_booksmodel"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BooksModel",
        ),
    ]
