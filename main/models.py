from django.db import models
from datetime import datetime
from modeltranslation.translator import TranslationOptions
from django.utils.translation import gettext_lazy as _

    
class Posts(models.Model):
    MY_CHOICES = (
        ("News", _("News")),
        ("Yangiliklar", _("Yangiliklar")),
        ("Articles", _("Articles")),
        ("Maqolalar", _("Maqolalar")),
        ("Scientific_Essays", _("Scientific Essays")),
        ("Ilmiy_tezislar", _("Ilmiy Tezislar")),
        ("Books", _("Books")),
        ("Kitoblar", _("Kitoblar")),
        ("International_Relations", _("International Relations")),
        ("Xalqaro_munosabatlar", _("Xalqaro munosabatlar")),
        ("Magazines", _("Magazines")),
        ("Jurnallar", _("Jurnallar")),
        ("Photo", _("Photos")),
        ("Foto_lavhalar", _("Foto Lavhalar")),
        ("Poetry", _("Poetry")),
        ("Sheriyat", _("She'riyat")),
        ("Stories", _("Stories")),
        ("Hikoyalar", _("Hikoyalar")),
        # ("Yol ocherklari", _("Yol_ocherklari")),
    )
    title = models.CharField(max_length=500)
    text = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.CharField(max_length=100, choices=MY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
class VideoModel(models.Model):
    title = models.CharField(max_length=500)
    video = models.FileField(upload_to="video/")
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

class BooksModel(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="books/")
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(verbose_name="Title", max_length=500)
    text = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.title
    

