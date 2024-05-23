from django.contrib import admin
from .models import Product, productImage
from django.utils.html import format_html

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


class imageAdmin(admin.ModelAdmin):
    list_display = ['display_image']

    def display_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 100px;" />')

    display_image.allow_tags = True
    display_image.short_description = 'Image'

admin.site.register(Product, productAdmin)
admin.site.register(productImage, imageAdmin)