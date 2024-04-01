from .models import Category

def product_categories(request):
    links = Category.objects.all()
    return {'links': links}