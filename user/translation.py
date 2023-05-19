from modeltranslation.translator import translator, TranslationOptions
from .models import MyModel

class MyModelTranslationOptions(TranslationOptions):
    fields = ('my_choice',)

translator.register(MyModel, MyModelTranslationOptions)


