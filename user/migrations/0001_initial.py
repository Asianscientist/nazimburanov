# Generated by Django 4.2.1 on 2023-05-25 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_choice', models.CharField(choices=[('News', 'News'), ('Yangiliklar', 'Yangiliklar'), ('Articles', 'Articles'), ('Maqolalar', 'Maqolalar'), ('Books', 'Books'), ('Kitoblar', 'Kitoblar')], max_length=500)),
            ],
        ),
    ]
