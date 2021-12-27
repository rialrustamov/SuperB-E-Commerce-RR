from django.urls import path

from . import views

urlpatterns = [
    path("faq/", views.faq, name="faq"),
    # path("homepage/", views.index, name="index"),
    path("404error/", views.error, name="404error"),
    path("about-us/", views.about_us, name="about_us"),
    path("address-book/", views.address_book, name="address_book"),
    path("contact-info/", views.contact_info, name="contact_info"),
    path("contact-us/", views.ContactUs.as_view(), name="contact_us"),
    path('set-language/', views.change_language, name="set_language"),
]
