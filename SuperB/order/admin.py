from django.contrib import admin

# Register your models here.

from order.models import Wishlist, ShoppingCart, CheckoutBilling, CartItem


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user', 'product')
    search_fields = ('user', 'product')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user',)
    search_fields = ('user',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity',)
    # list_filter = ('user',)
    # search_fields = ('user',)
    list_editable = ('quantity',)


@admin.register(CheckoutBilling)
class CheckoutBillingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'email', 'address', 'country', 'telephone',)
    list_filter = ('first_name', 'last_name', 'company', 'email', 'address', 'country', 'telephone',)
    search_fields = ('first_name', 'last_name', 'company', 'email', 'address', 'country', 'telephone',)