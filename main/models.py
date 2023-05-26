from django.db import models
from datetime import datetime
from modeltranslation.translator import TranslationOptions
from django.utils.translation import gettext_lazy as _

    
class Posts(models.Model):
    MY_CHOICES = (
        ("News", "News"),
        ("Yangiliklar", "Yangiliklar"),
        ("Articles", "Articles"),
        ("Maqolalar", "Maqolalar"),
        ("Scientific_Essays", "Scientific Essays"),
        ("Ilmiy_tezislar", "Ilmiy Tezislar"),
        ("Books", "Books"),
        ("Kitoblar", "Kitoblar"),
        ("International_Relations", "International Relations"),
        ("Xalqaro_munosabatlar", "Xalqaro munosabatlar"),
        ("Magazines", "Magazines"),
        ("Jurnallar", "Jurnallar"),
        ("Photos", "Photos"),
        ("Foto_lavhalar", "Foto Lavhalar"),
        ("Poetry", "Poetry"),
        ("Sheriyat", "She'riyat"),
        ("Stories", "Stories"),
        ("Hikoyalar", "Hikoyalar"),
        # ("Yol ocherklari", "Yol_ocherklari"),
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


