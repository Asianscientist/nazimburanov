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
    picture = models.ImageField(upload_to='images/')
    picture2 = models.ImageField(upload_to='images/', null=True, blank=True)
    picture3 = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.CharField(max_length=100, choices=MY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
class VideoModel(models.Model):
    title = models.CharField(max_length=500)
    video = models.FileField(upload_to="video/")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

class BooksModel(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()
    file = models.FileField(upload_to="books/")
    
    def __str__(self):
        return self.title

class CertificateModel(models.Model):
    picture = models.ImageField(upload_to='certificates/')
    text = models.TextField()

    def __str__(self):
        return self.text[:100]
    
    
