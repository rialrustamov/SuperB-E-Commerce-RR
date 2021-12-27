from django.shortcuts import render, redirect, resolve_url
from django.db.models import Q
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from product.models import *
from core.forms import *
from blog.models import *
from django.db.models import Count

from core.models import *


# Create your views here.

def faq(request):

    faqs = Faq.objects.all()

    context = {
        'faqs': faqs,
        'title' : 'FAQ',
    }

    return render(request, 'faq.html', context=context)


def index(request):

    products = ProductVersion.objects.all()
    most_rev = Product.objects.annotate(num_coms=Count('product_review')).order_by('-num_coms')[:4]
    blogs =  Blog.objects.order_by('-id')[:2]
    last_products = Product.objects.order_by('-id')[:4]

    context = {
        'products': products,
        'title' : 'HOMEPAGE',
        'most_rev': most_rev,
        'blogs': blogs,
        'last_products': last_products      
    }

    return render(request, 'index.html', context=context)


def error(request):

    context = {
        'title' : '404 error',
    }

    return render(request, "404error.html", context=context)


def about_us(request):

    context = {
        'title' : 'About Us',
    }

    return render(request, "about_us.html", context=context)


def address_book(request):

    context = {
        'title' : 'Address Book',
    }

    return render(request, "address_book.html", context=context)


def contact_info(request):
    if request.method == "POST":
        form = ContactInfoRequestForm(request.POST or None)
        if form.is_valid():
            if ContactInfo.objects.filter(user_contact_info=request.user).exists() == False:
                contact_info = ContactInfo(
                    first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                    company=request.POST.get('company'),
                    telephone=request.POST.get('telephone'),
                    fax=request.POST.get('fax'),
                    address_one=request.POST.get('address_one'),
                    address_two=request.POST.get('address_two'),
                    zip=request.POST.get('zip'),
                    country=request.POST.get('country'),
                    user_contact_info=request.user
                )
                contact_info.save()
            else:
                ContactInfo.objects.filter(user_contact_info=request.user).update(first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                    company=request.POST.get('company'),
                    telephone=request.POST.get('telephone'),
                    fax=request.POST.get('fax'),
                    address_one=request.POST.get('address_one'),
                    address_two=request.POST.get('address_two'),
                    zip=request.POST.get('zip'),
                    country=request.POST.get('country'),)
                # return redirect(address_book)
    else:
        form = ContactInfoRequestForm()

    context = {
        'title' : 'Contact Information',
        'form' : form,
    }
    return render(request, "contact_information.html", context=context)


def contact_us(request):

    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(contact_us)
        else:
            print(form.errors)
    else:
        form = ContactUsForm()

    context = {
        'title' : 'Contact Us',
        'form' : form,
    }

    return render(request, "contact_us.html", context=context)


#Generic views

class ContactUs(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = "contact_us.html"

    def get_success_url(self):
        return resolve_url('contact_us')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Contact Us"

        return context



def change_language(request):
    if request.GET.get('lang') == 'en' or request.GET.get('lang') == 'az':
        # print(request.META.get('HTTP_REFERER'))
        path_list = request.META.get('HTTP_REFERER').split('/')
        # print(path_list)
        path_list[3] = request.GET.get('lang')
        path = '/'.join(path_list)
        # print(path)
        
        response = HttpResponseRedirect(path)
        response.set_cookie('django_language', request.GET['lang'])
        return response