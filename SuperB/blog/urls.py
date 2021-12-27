from django.urls import path

from . import views

urlpatterns = [
    # path("blog/", views.blog, name="blog"),
    path("blog-detail/<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("blog/", views.BlogList.as_view(), name="blog"),
    # path("blog-detail/", views.blog_detail, name="blog_detail"),
]
