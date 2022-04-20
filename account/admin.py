from django.contrib import admin
from .models import UserRegisterModel
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


@admin.register(UserRegisterModel)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom UserRegister model with no phone number field"""
    
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password'),
        }),
    )
    list_display = ('phone', 'first_name', 'last_name', 'is_staff')
    search_fields = ('phone', 'first_name', 'last_name')
    ordering = ('phone',)