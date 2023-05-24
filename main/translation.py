from .models import Posts, VideoModel, Product, BooksModel
from django.contrib import admin
from modeltranslation.translator import TranslationOptions, register, translator


@register(Posts)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text', "category")
    required_languages = ("en","uz")

# translator.register(Posts, PostTranslationOptions)


@register(BooksModel)
class BooksTranslationOptions(TranslationOptions):
    fields = ("title", "text")