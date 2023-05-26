from django.contrib import admin
from .models import Posts, VideoModel
from .translation import PostTranslationOptions, BooksModel
from modeltranslation.admin import TranslationAdmin

@admin.register(Posts)
class PostAdmin(TranslationAdmin):
    list_display = ("title","text","category")
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(BooksModel)
class BooksAdmin(TranslationAdmin):
    list_display = ("title", "text")


@admin.register(VideoModel)
class VideoAdmin(TranslationAdmin):
    list_display = ("title", "text")
