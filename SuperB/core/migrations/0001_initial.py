# Generated by Django 3.2.7 on 2021-11-23 16:39

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(help_text='Max 255 character', max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(help_text='Max 255 character', max_length=50, verbose_name='Last Name')),
                ('company', models.TextField(verbose_name='Company')),
                ('telephone', models.CharField(max_length=25, verbose_name='Telephone')),
                ('fax', models.CharField(max_length=50, verbose_name='Fax')),
                ('address_one', models.TextField(verbose_name='Street Address')),
                ('address_two', models.TextField(verbose_name='Street Address 2')),
                ('zip', models.CharField(max_length=255, verbose_name='Zip/Postal Code')),
                ('country', django_countries.fields.CountryField(max_length=255, verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Contact Info',
                'verbose_name_plural': 'All Contacts Info',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(help_text='Max 255 character', max_length=50, verbose_name='First Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('company', models.TextField(blank=True, null=True, verbose_name='Company')),
                ('telephone', models.CharField(max_length=25, verbose_name='Telephone')),
                ('address_one', models.TextField(verbose_name='Address_one')),
                ('address_two', models.TextField(blank=True, null=True, verbose_name='Addres_two')),
                ('comment', models.TextField(verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.TextField(verbose_name='Question')),
                ('answer', models.TextField(verbose_name='Answer')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQ',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
            },
        ),
    ]
