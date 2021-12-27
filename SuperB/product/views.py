from django.shortcuts import render, redirect, resolve_url
from django.http import JsonResponse
from django.db.models import Q
from django.views.generic import View, TemplateView, DetailView, ListView, CreateView, UpdateView, FormView
from django.views.generic.edit import DeleteView

import json

from django.http import HttpResponseRedirect



from product.forms import *
from django.db.models import Count
from product.models import *


def product_detail(request, pk): 

    product = Product.objects.get(pk=pk)
    qs = Product.objects.all()

    if request.method == "POST":
        form = ReviewRequestForm(request.POST or None)
        if form.is_valid():
            review = Review(
                product = Product.objects.get(pk=pk),
                price_rating=request.POST.get('price_rating'),
                value_rating=request.POST.get('value_rating'),
                quality_rating=request.POST.get('quality_rating'),
                nickname=request.POST.get('nickname'),
                summary=request.POST.get('summary'),
                review=request.POST.get('review'),
            )
            review.save()
            return redirect(product_list) #burada product_detail yazanda ishlemir. Baxmaq lazimdir.
    else:
        form = ReviewRequestForm()

    context = {
        'title' : "Product's Detail",
        'product' : product,
        'qs' : qs,
        'form' : form,
    }
    return render(request, 'product-detail.html', context=context)


def product_list(request):

    pop_tags = Tag.objects.annotate(num_tags=Count('product_tags')).order_by('-num_tags')[:1]
    qs = Product.objects.all()
    context = {
        'title' : 'Product Lists',
        'products' : qs,
        'popular_tags' : pop_tags,
        'categories' : Category.objects.all()
    }

    return render(request, 'product-list.html', context=context)


#Generic Views
class ProductDetail(DetailView):
    model = ProductVersion
    template_name = 'product-detail.html'

    def get_object(self):
        return ProductVersion.objects.get(pk=self.kwargs['pk'])

    def related_object(self):
        return ProductVersion.objects.exclude(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Product's Detail"
        context['product'] = self.get_object()
        context['qs'] = self.related_object()
        context['form'] = ReviewRequestForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewRequestForm(request.POST, request.FILES)
        if form.is_valid():
            review = Review(
                product = self.get_object().product,
                user_review=request.user,
                price_rating=request.POST.get('price_rating'),
                value_rating=request.POST.get('value_rating'),
                quality_rating=request.POST.get('quality_rating'),
                nickname=request.POST.get('nickname'),
                summary=request.POST.get('summary'),
                review=request.POST.get('review'),
            )
            review.save()

            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = ReviewRequestForm
            return HttpResponseRedirect(self.request.path_info)
            

        else:
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = ReviewRequestForm
            return self.render_to_response(context=context)


class ProductList(ListView):
    model = ProductVersion
    template_name = 'product-list.html'
    paginate_by = 2
    context_object_name = 'products'

    def get_queryset(self):
        products = ProductVersion.objects.filter(is_main=True)
        if self.request.GET.get("search"):
            products = products.filter( Q(product__title__icontains=self.request.GET.get("search")) | Q(
                product__category__title__icontains=self.request.GET.get("search")) | Q(product__brand__title__icontains=self.request.GET.get("search")))
        if self.request.GET.get("category_title"):
            products = products.filter(
                product__category__title=self.request.GET.get("category_title"))
        if self.request.GET.get("parent_title"):
            products = products.filter(
                product__category__parent__title=self.request.GET.get("parent_title"))
        if self.request.GET.get("max_price"):
            products = products.filter(
                product__discount_price__lte = 200
            )
        if self.request.GET.get("min_price"):
            products = products.filter(
                product__discount_price__gte = 200 
            )
        if self.request.GET.get("color"):
            products = products.filter(
                color__title=self.request.GET.get("color")
            )
        if self.request.GET.get("size"):
            products = products.filter(
                size__title=self.request.GET.get("size")
            )
        
        return products
        

    def categories(self):
        categories = Category.objects.all()

        return categories
    
    def colors(self):
        colors = Color.objects.all()
        return colors

    def sizes(self):
        sizes = Size.objects.all()
        return sizes

    def get_most_popular(self):
        most_popular = Tag.objects.annotate(num_tags=Count('product_tags')).order_by('-num_tags')[:3]

        return most_popular

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Product's List"
        # context['products'] = self.get_queryset()
        context['categories'] = self.categories()
        context['colors'] = self.colors()
        context['sizes'] = self.sizes()
        context['most_popular'] = self.get_most_popular()

        return context

class Search(ListView):

    model = ProductVersion
    template_name = 'search.html'
    context_object_name = 'products'

    def get_queryset(self):
        products = super(Search, self).get_queryset()
        if self.request.GET.get("search"):
            products = products.filter( Q(product__title__icontains=self.request.GET.get("search")) | Q(
            product__category__title__icontains=self.request.GET.get("search")) | Q(product__brand__title__icontains=self.request.GET.get("search")))
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['word'] = self.request.GET.get("search")
        context['title'] = 'Search Results'
        return context
