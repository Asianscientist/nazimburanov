# Generated by Django 4.2.1 on 2023-05-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_posts_category_en_posts_category_uz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.CharField(choices=[('News', 'News'), ('Yangiliklar', 'Yangiliklar'), ('Articles', 'Articles'), ('Maqolalar', 'Maqolalar'), ('CountryImage', 'Image of the Country'), ('Mamlakat_Imiji', 'Mamlakat Imiji'), ('Scientific_Articles', 'Scientific Articles'), ('Ilmiy_Maqolalar', 'Ilmiy Maqolalar'), ('Books', 'Books'), ('Kitoblar', 'Kitoblar'), ('International_Projects', 'International Projects'), ('Xalqaro_Loyihalar', 'Xalqaro Loyihalar'), ('Announcement', 'Announcement'), ('Anons', 'Anons'), ('Phd_Aftoreferati', 'Phd Aftoreferati'), ('Phd_Aftoreferati', 'Phd Aftoreferati'), ('Scientific_Research', 'Scientific Research'), ('Ilmiy_tadqiqot', 'Ilmiy Tadqiqot'), ('Magazines', 'Magazines'), ('Jurnallar', 'Jurnallar'), ('Foreign_Journals', 'Foreign Journals'), ('Collections', 'Collections'), ('Kolleksiyalar', 'Kolleksiyalar'), ('Training', 'Training'), ('Trening', 'Trening'), ('Workshops', 'Workshops'), ('Workshoplar', 'Workshoplar'), ('Speeches', 'Speeches'), ('Nutqlar', 'Nutqlar'), ('Prezentatsiyalar', 'Prezentatsiyalar')], max_length=50),
        ),
        migrations.AlterField(
            model_name='posts',
            name='category_en',
            field=models.CharField(choices=[('News', 'News'), ('Yangiliklar', 'Yangiliklar'), ('Articles', 'Articles'), ('Maqolalar', 'Maqolalar'), ('CountryImage', 'Image of the Country'), ('Mamlakat_Imiji', 'Mamlakat Imiji'), ('Scientific_Articles', 'Scientific Articles'), ('Ilmiy_Maqolalar', 'Ilmiy Maqolalar'), ('Books', 'Books'), ('Kitoblar', 'Kitoblar'), ('International_Projects', 'International Projects'), ('Xalqaro_Loyihalar', 'Xalqaro Loyihalar'), ('Announcement', 'Announcement'), ('Anons', 'Anons'), ('Phd_Aftoreferati', 'Phd Aftoreferati'), ('Phd_Aftoreferati', 'Phd Aftoreferati'), ('Scientific_Research', 'Scientific Research'), ('Ilmiy_tadqiqot', 'Ilmiy Tadqiqot'), ('Magazines', 'Magazines'), ('Jurnallar', 'Jurnallar'), ('Foreign_Journals', 'Foreign Journals'), ('Collections', 'Collections'), ('Kolleksiyalar', 'Kolleksiyalar'), ('Training', 'Training'), ('Trening', 'Trening'), ('Workshops', 'Workshops'), ('Workshoplar', 'Workshoplar'), ('Speeches', 'Speeches'), ('Nutqlar', 'Nutqlar'), ('Prezentatsiyalar', 'Prezentatsiyalar')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='category_uz',
            field=models.CharField(choices=[('News', 'News'), ('Yangiliklar', 'Yangiliklar'), ('Articles', 'Articles'), ('Maqolalar', 'Maqolalar'), ('CountryImage', 'Image of the Country'), ('Mamlakat_Imiji', 'Mamlakat Imiji'), ('Scientific_Articles', 'Scientific Articles'), ('Ilmiy_Maqolalar', 'Ilmiy Maqolalar'), ('Books', 'Books'), ('Kitoblar', 'Kitoblar'), ('International_Projects', 'International Projects'), ('Xalqaro_Loyihalar', 'Xalqaro Loyihalar'), ('Announcement', 'Announcement'), ('Anons', 'Anons'), ('Phd_Aftoreferati', 'Phd Aftoreferati'), ('Phd_Aftoreferati', 'Phd Aftoreferati'), ('Scientific_Research', 'Scientific Research'), ('Ilmiy_tadqiqot', 'Ilmiy Tadqiqot'), ('Magazines', 'Magazines'), ('Jurnallar', 'Jurnallar'), ('Foreign_Journals', 'Foreign Journals'), ('Collections', 'Collections'), ('Kolleksiyalar', 'Kolleksiyalar'), ('Training', 'Training'), ('Trening', 'Trening'), ('Workshops', 'Workshops'), ('Workshoplar', 'Workshoplar'), ('Speeches', 'Speeches'), ('Nutqlar', 'Nutqlar'), ('Prezentatsiyalar', 'Prezentatsiyalar')], max_length=50, null=True),
        ),
    ]
