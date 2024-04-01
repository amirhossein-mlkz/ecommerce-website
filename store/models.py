from django.db import models
from category.models import Category
# Create your models here.
class Product(models.Model):

    name          = models.CharField( max_length=50)
    slug          = models.SlugField( unique=True)
    description   = models.TextField(blank=True)
    price         = models.DecimalField( max_digits=20, decimal_places=0)
    image         = models.ImageField(upload_to='photos/product', blank=True)
    stock         = models.IntegerField()
    is_available  = models.BooleanField(default=True)
    category      = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date  = models.DateTimeField( auto_now_add=True)
    modified_date = models.DateTimeField( auto_now=True)


    def __str__(self) -> str:
        return self.name

