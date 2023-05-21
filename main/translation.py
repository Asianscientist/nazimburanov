from .models import Posts, SuggestionModel, VideoModel, Product, BooksModel
from django.contrib import admin
from modeltranslation.translator import TranslationOptions, register, translator


@register(Posts)
class PostTranslationOptions(TranslationOptions):
    fields = ['title', 'text', "category"]

# translator.register(Posts, PostTranslationOptions)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("title", "text")

@register(BooksModel)
class BooksTranslationOptions(TranslationOptions):
    fields = ("title", "text")