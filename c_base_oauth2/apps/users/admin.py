from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdmin(BaseUserAdmin):
    """Define a new User admin"""
    fieldsets = BaseUserAdmin.fieldsets\
        + ((_('LDAP account'), {'fields': ('uid', )}), )\
        + ((_('Alien account'), {'fields': ('is_temporary_alien', 'valid_until')}), )


admin.site.register(User, UserAdmin)
