from django.contrib import admin
from django.contrib.admin import ModelAdmin

from pets.models import Pet


@admin.register(Pet)
class PetAdmin(ModelAdmin):
    list_display = ['name', 'slug']