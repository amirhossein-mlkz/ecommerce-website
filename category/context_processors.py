from .models import Category

def product_categories(request):
    cats = Category.objects.all()
    return {'product_categories': cats}