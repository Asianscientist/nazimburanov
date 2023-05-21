from django.contrib import admin
from .models import Posts, VideoModel, Product
from .translation import PostTranslationOptions, BooksModel
from modeltranslation.admin import TranslationAdmin

@admin.register(Posts)
class PostAdmin(TranslationAdmin):
    list_display = ('title', "text", "category")

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    fields = ("title", "text")

@admin.register(BooksModel)
class BooksAdmin(TranslationAdmin):
    list_display = ("title", "text")
