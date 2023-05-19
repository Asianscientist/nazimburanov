from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

    
class Posts(models.Model):
    MY_CHOICES = (
        ("NEWS", 'News'),
        ("ARTICLES", 'Articles'),
        ("COUNTRYIMAGE", 'Image of the Country'),
        ("SCIENTIFIC_ARTICLES", "Scientific Articles"),
        ("BOOKS", "Books"),
        ("INTERNATIONAL_PROJECTS", "International Projects"),
        ("ANNOUNCEMENT", "Announcement"),
        ("PHD_AFTOREFERAT", "Phd Aftoreferati"),
        ("SCIENTIFIC_RESEARCH", "Scientific Research"),
        ("MAGAZINES", "Magazines"),
        ("FOREIGN_JOURNALS", "Foreign Journals"),
        ("COLLECTIONS", "Collections"),
        ("TRAINING", "Training"),
        ("WORKSHOPS", "Workshops"),
        ("SPEECHES", "Speeches"),
        ("PRESENTATIONS", "Presentations")
    )
    title = models.CharField(_(max_length=500))
    text = models.TextField()
    picture = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=50, choices=MY_CHOICES)
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