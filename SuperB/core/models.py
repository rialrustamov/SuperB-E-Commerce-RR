from django.db import models

from SuperB.utils.base import BaseModel
from django_countries.fields import CountryField

class ContactInfo(BaseModel):
    first_name = models.CharField(max_length=50,verbose_name='First Name', help_text='Max 255 character')
    last_name = models.CharField(max_length=50,verbose_name='Last Name', help_text='Max 255 character')
    company = models.TextField(verbose_name='Company')
    telephone = models.CharField(max_length=25 ,verbose_name='Telephone')
    fax = models.CharField(max_length=50, verbose_name='Fax')
    address_one = models.TextField(verbose_name='Street Address')
    address_two = models.TextField(verbose_name='Street Address 2')
    zip = models.CharField(max_length=255, verbose_name='Zip/Postal Code')
    country = CountryField(max_length=255, verbose_name='Country')
    user_contact_info = models.OneToOneField('user.User', on_delete=models.CASCADE, max_length=255, help_text='Max 255 chars', related_name='user_contactinfo', verbose_name="User", null=True, blank=True)

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "All Contacts Info"

    def __str__(self):
        return self.first_name

class Faq(BaseModel):
    question = models.TextField(verbose_name='Question')
    answer = models.TextField(verbose_name='Answer')

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"

    def __str__(self):
        return f'{self.question, self.answer}'

class ContactUs(BaseModel):
    first_name = models.CharField(max_length=50,verbose_name='First Name', help_text='Max 255 character')
    email = models.EmailField(verbose_name='Email Address')
    company = models.TextField(verbose_name='Company', null=True, blank=True)
    telephone = models.CharField(max_length=25 ,verbose_name='Telephone')
    address_one = models.TextField(verbose_name='Address_one')
    address_two = models.TextField(verbose_name='Addres_two', null=True, blank=True)
    comment = models.TextField(verbose_name='Comment')

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.first_name


class Subscriber(BaseModel):
    email = models.EmailField(verbose_name='Email Address')

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"

    def __str__(self):
        return self.email





