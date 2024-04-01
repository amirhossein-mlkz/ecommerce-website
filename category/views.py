from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.


def single_category(request, the_slug):
    print(the_slug)
    template = loader.get_template('single_cat.html')

    context = {
        'title': the_slug,
    }

    return HttpResponse(template.render(context, request))


def archive_category(request):
    template = loader.get_template('archive_cats.html')
    return HttpResponse(template.render())