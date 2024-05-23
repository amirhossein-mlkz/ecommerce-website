from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Product
from category.models import Category


# Create your views here.
def store(request, category_slug=None):
    if category_slug is None:
        products = Product.objects.all()
    else:
        cat = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=cat)
    
    template = loader.get_template('store.html')

    context = {
        'all_products': products
    }


    return HttpResponse( template.render(context, request))



def product_details(request, category_slug=None, product_slug=None):

    #product = get_object_or_404(Product, slug=product_slug)
    try:
        #.get methed return one and only one object but .filter return mulit object or empty list
        # category__slug means slug atribut of category model of this product (category is foriegin key)
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        print(e)
        product = None
    template = loader.get_template('product-details.html')


    context = {
        'product': product
    }


    return HttpResponse( template.render(context, request))