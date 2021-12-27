# Generated by Django 3.2.7 on 2021-11-23 16:39

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CheckoutBilling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(help_text='Max 255 character', max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(help_text='Max 255 character', max_length=50, verbose_name='Last Name')),
                ('company', models.TextField(verbose_name='Company')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('address', models.TextField(verbose_name='Street Address')),
                ('country', django_countries.fields.CountryField(max_length=255, verbose_name='Country')),
                ('telephone', models.CharField(max_length=25, verbose_name='Telephone')),
                ('fax', models.CharField(max_length=50, verbose_name='Fax')),
            ],
            options={
                'verbose_name': 'Checkout Billing',
                'verbose_name_plural': 'Checkout Billings',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_ordered', models.BooleanField(default=False, verbose_name='Is ordered?')),
            ],
            options={
                'verbose_name': 'Shopping Cart',
                'verbose_name_plural': 'Shopping Carts',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Wishlist',
                'verbose_name_plural': 'Wishlists',
            },
        ),
    ]
