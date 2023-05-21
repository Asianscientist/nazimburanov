# Generated by Django 4.1 on 2023-05-20 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0011_delete_booksmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="BooksModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=500)),
                ("title_en", models.CharField(max_length=500, null=True)),
                ("title_uz", models.CharField(max_length=500, null=True)),
                ("text", models.TextField()),
                ("text_en", models.TextField(null=True)),
                ("text_uz", models.TextField(null=True)),
                ("file", models.FileField(upload_to="books/")),
            ],
        ),
    ]
