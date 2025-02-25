from django.db import models
from datetime import datetime
    
class Posts(models.Model):
    MY_CHOICES = (
        # ("News", "News"),
        ("Yangiliklar", "Yangiliklar"),
        # ("Articles", "Articles"),
        ("Maqolalar", "Maqolalar"),
        # ("Scientific_Essays", "Scientific Essays"),
        ("Ilmiy_Maqolalar", "Ilmiy Maqolalar"),
        ("Xalqaro_munosabatlar", "Xalqaro munosabatlar"),
        ("Jurnallar", "Jurnallar"),
        ("Foto_lavhalar", "Foto Lavhalar"),
        ("Sheriyat", "She'riyat"),
        ("Hikoyalar", "Hikoyalar"),
        ("Yol_ocherklari", "Yo'l ocherklari"),
    )
    title = models.CharField(max_length=500)
    text = models.TextField()
    author = models.CharField(null=True, blank=True, max_length=500)
    picture = models.ImageField(upload_to='images/')
    picture2 = models.ImageField(upload_to='images/', null=True, blank=True)
    picture3 = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.CharField(max_length=100, choices=MY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
class VideoModel(models.Model):
    title = models.CharField(max_length=500)
    video = models.URLField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

class BooksModel(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()
    author = models.CharField(null=True, blank=True, max_length=500)
    file = models.FileField(upload_to="books/")
    
    def __str__(self):
        return self.title

class CertificateModel(models.Model):
    picture = models.ImageField(upload_to='certificates/')
    file = models.FileField(upload_to='certificates/', null=True, blank=True)

    def __str__(self):
        return self.picture.name
    
