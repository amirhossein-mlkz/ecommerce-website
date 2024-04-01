from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
# Create your views here.

def home(request):
    template = get_template('home.html')
    
    #we should pass a context to work context_presorcess
    return HttpResponse(template.render({}, request))