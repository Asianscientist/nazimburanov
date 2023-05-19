from .models import Posts, SuggestionModel, VideoModel, Product
from django.contrib import admin
from modeltranslation.translator import TranslationOptions, register, translator
from modeltranslation.admin import TranslationAdmin


@register(Posts)
class PostTranslationOptions(TranslationOptions):
    fields = ['title', 'text', "category"]

# translator.register(Posts, PostTranslationOptions)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("title", "text")

