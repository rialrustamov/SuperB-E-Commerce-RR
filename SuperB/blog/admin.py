from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from blog.models import Blog, Comment, Category



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description')
    list_filter = ('title', 'author')
    search_fields = ('title', 'author')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'message')
    list_filter = ('author', 'message')
    search_fields = ('author', 'message')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (['title'])
    list_filter = (['title'])
    search_fields = (['title'])


