from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
    #     }),
    # )
    pass
# from django.contrib import admin
#
#
# @admin.register(Permission)
# class PermissionAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
