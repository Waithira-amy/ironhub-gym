from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Gym Profile", {"fields": ("role", "bio", "fitness_goal", "avatar")}),
    )
    list_display = ("username", "email", "role", "is_staff")
    list_filter = ("role", "is_staff")