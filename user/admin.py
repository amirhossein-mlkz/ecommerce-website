from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.models import User as bUser
# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ('firstname', 'lastname', 'phone_number')
    list_display_links = ('firstname', 'lastname')
    readonly_fields = ('last_login', 'joinied_date')
    list_filter = tuple()
    filter_horizontal = tuple()
    ordering = ('-joinied_date',)
    
#admin.site.unregister(bUser)
admin.site.register(User, UserAdmin)
#admin.site.register(User)
