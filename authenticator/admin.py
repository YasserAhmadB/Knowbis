from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "first_name", "last_name"),
            },
        ),
    )

    list_display = ("username", "email", "first_name", "last_name", "is_staff")
