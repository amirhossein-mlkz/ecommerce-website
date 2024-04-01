from django.contrib import admin
from .models import Product

class productAdmin(admin.ModelAdmin):
    list_display = ('name', 
                    'slug', 
                    'price', 
                    'stock', 
                    'is_available', 
                    'category', 
                    'created_date', 
                    'modified_date'
                    )
    
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product, productAdmin)