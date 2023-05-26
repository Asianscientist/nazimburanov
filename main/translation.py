from .models import Posts, VideoModel, BooksModel
from django.contrib import admin
from modeltranslation.translator import TranslationOptions, register, translator


@register(Posts)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text', "category")
    required_languages = ("en","uz")


@register(BooksModel)
class BooksTranslationOptions(TranslationOptions):
    fields = ("title", "text")


@register(VideoModel)
class VideoTranslationOptions(TranslationOptions):
    fields = ("title", "text")

