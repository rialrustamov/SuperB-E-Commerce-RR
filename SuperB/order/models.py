from django.db import models

from SuperB.utils.base import BaseModel
from django_countries.fields import CountryField

# Create your models here.


class ShoppingCart(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, max_length=255, help_text='Max 255 chars', related_name='user_cart', verbose_name="User", null=True, blank=True)
    product = models.ManyToManyField('product.ProductVersion', related_name="carts", verbose_name="ProductCart", blank=True)
    is_ordered = models.BooleanField(verbose_name="Is ordered?", default=False)
    shipping_address = models.ForeignKey('order.CheckoutBilling', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Shopping Cart"
        verbose_name_plural = "Shopping Carts"

    def __str__(self):
        return f'{self.user}'


class CartItem(BaseModel):
    cart = models.ForeignKey(ShoppingCart, related_name="cart_item", on_delete=models.CASCADE)
    product = models.ForeignKey(
        'product.ProductVersion', related_name="cart_product", on_delete=models.CASCADE
    )
    quantity = models.IntegerField(default=0)


class Wishlist(BaseModel):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE, max_length=255, 
        help_text='Max 255 chars', related_name='user_wishlist', verbose_name="User", null=True, blank=True)
    product = models.ManyToManyField('product.ProductVersion', related_name="wishlist", verbose_name="ProductWishlist", blank=True)

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"

    def __str__(self):
        return f'{self.user}'

        
class CheckoutBilling(BaseModel):
    first_name = models.CharField(max_length=50,verbose_name='First Name', help_text='Max 255 character')
    last_name = models.CharField(max_length=50,verbose_name='Last Name', help_text='Max 255 character')
    company = models.TextField(verbose_name='Company')
    email = models.EmailField(verbose_name='Email Address')
    address = models.TextField(verbose_name='Street Address')
    country = CountryField(max_length=255, verbose_name='Country')
    telephone = models.CharField(max_length=25 ,verbose_name='Telephone')
    fax = models.CharField(max_length=50, verbose_name='Fax')
    user_billing_info = models.ForeignKey('user.User', on_delete=models.CASCADE, max_length=255, help_text='Max 255 chars', related_name='user_checkout', verbose_name="User", null=True, blank=True)


    class Meta:
        verbose_name = "Checkout Billing"
        verbose_name_plural = "Checkout Billings"

    def __str__(self):
        return self.first_name
