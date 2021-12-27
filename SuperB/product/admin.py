from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from product.models import Product, Brand, ProductVersion, Tag, Review, Category, Image, Color, Size


admin.site.site_header = 'SuperB'
admin.site.site_title = 'SuperB'


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    search_fields = ['tag']


# class BrandInline(admin.TabularInline):
#     model = Brand
#     extra = 1


# class ProductInline(admin.StackedInline):
#     model = Product
#     extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price', 'brand', 'category')
    list_filter = ('title', 'brand__title')
    search_fields = ('title', 'brand__title', 'review', 'price')
    autocomplete_fields = ['product_tag']

    # fieldsets = (
    #     ("General Informations", {'fields' : ('title', 'review', 'brand')}),
    #     ("Price", {'fields' : ('price', 'discount_price')}),
    # )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'color', 'size', 'quantity', 'is_main',)
    list_filter = ('product', 'color', 'size',)
    search_fields = ('product', 'color', 'size', 'quantity')
    # inlines = [ProductInline]



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('get_image',)
    list_filter = ('image',)
    search_fields = ('image',)

    def get_image(self,obj):
        if obj.image:
            img = '<img src="{}" width="100" height="100" />'.format(obj.image.url)
            return format_html(img)
        return 'No Image'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ( 'product', 'price_rating', 'value_rating', 'quality_rating', 'nickname', 'summary', 'review')
    list_filter = ('price_rating', 'value_rating', 'quality_rating', 'nickname', 'summary', 'review',)
    search_fields = ('price_rating', 'value_rating', 'quality_rating', 'nickname', 'summary', 'review',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)