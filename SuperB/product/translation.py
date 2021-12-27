from django.db.models import fields
from modeltranslation.translator import register, TranslationOptions

from product.models import Category

@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('title',)