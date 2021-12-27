from django.urls import path

from . import views

urlpatterns = [
    path("quick-view/", views.quick_view, name="quick_view"),
    path("shopping-cart/", views.shopping_cart, name="shopping_cart"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("checkout/", views.checkout, name="checkout"),
    path("checkout-bill/", views.checkout_bill, name="checkout_bill"),
    path("result/", views.result, name="result")
]
