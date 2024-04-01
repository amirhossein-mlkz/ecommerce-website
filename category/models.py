from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, blank = False, unique = True)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to='photos/category')
    
    #class Meta define labels show in admin panell menu
    class Meta:
        #db_table = ''
        #managed = True
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_url(self,):
        return reverse( 'store_by_category', args=(self.slug,))

    def __str__(self) -> str:
        return self.name