from django.contrib import admin

# Register your models here.

from core.models import ContactInfo, Faq, ContactUs, Subscriber



@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'telephone',)
    list_filter = ('first_name', 'last_name', 'company', 'telephone',)
    search_fields = ('first_name', 'last_name' ,'company', 'telephone',)

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    list_filter = ('question', 'answer')
    search_fields = ('question', 'answer')

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'company', 'telephone', 'address_one')
    list_filter = ('first_name', 'email', 'company', 'telephone', 'address_one')
    search_fields = ('first_name', 'email', 'company', 'telephone', 'address_one')


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (['email'])
    list_filter = (['email'])
    search_fields = (['email'])
