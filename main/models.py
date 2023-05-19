from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
    
class Posts(models.Model):
    MY_CHOICES = (
        ("News", _("News")),
        ("Yangiliklar", _("Yangiliklar")),
        ("Articles", _("Articles")),
        ("Maqolalar", _("Maqolalar")),
        ("CountryImage", _("Image of the Country")),
        ("Mamlakat_Imiji", _("Mamlakat Imiji")),
        ("Scientific_Articles", _("Scientific Articles")),
        ("Ilmiy_Maqolalar", _("Ilmiy Maqolalar")),
        ("Books", _("Books")),
        ("Kitoblar", _("Kitoblar")),
        ("International_Projects", _("International Projects")),
        ("Xalqaro_Loyihalar", _("Xalqaro Loyihalar")),
        ("Announcement", _("Announcement")),
        ("Anons", _("Anons")),
        ("Phd_Aftoreferati", _("Phd Aftoreferati")),
        ("Phd_Aftoreferati", _("Phd Aftoreferati")),
        ("Scientific_Research", _("Scientific Research")),
        ("Ilmiy_tadqiqot", _("Ilmiy Tadqiqot")),
        ("Magazines", _("Magazines")),
        ("Jurnallar", _("Jurnallar")),
        ("Foreign_Journals", _("Foreign Journals")),
        ("Collections", _("Collections")),
        ("Kolleksiyalar", _("Kolleksiyalar")),
        ("Training", _("Training")),
        ("Trening", _("Trening")),
        ("Workshops", _("Workshops")),
        ("Workshoplar", _("Workshoplar")),
        ("Speeches", _("Speeches")),
        ("Nutqlar", _("Nutqlar")),
        ("Prezentatsiyalar", _("Prezentatsiyalar"))
    )
    title = models.CharField(max_length=500)
    text = models.TextField()
    picture = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=50, choices=MY_CHOICES, )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class SuggestionModel(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()
    picture = models.ImageField(upload_to="suggestions/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
class VideoModel(models.Model):
    title = models.CharField(max_length=500)
    video = models.FileField(upload_to="video/")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

class BooksModel(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()
    file = models.FileField(upload_to="books/")

class Product(models.Model):
    title = models.CharField(verbose_name="Title", max_length=500)
    text = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.title
    

