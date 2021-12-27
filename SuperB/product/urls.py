from django.urls import path

from . import views

urlpatterns = [
    path("product-detail/<int:pk>/", views.ProductDetail.as_view(), name="product_detail"),
    path("product-list/", views.ProductList.as_view(), name="product_list"),
    path("search/", views.Search.as_view(), name="search"),
]