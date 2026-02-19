from django.contrib import admin
from django.contrib.admin import ModelAdmin

from photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(ModelAdmin):
    list_display = ['id', 'description', 'date_of_publication', 'tagged_pets_list']

    @classmethod
    def tagged_pets_list(cls, obj):
        return ' '.join(pet.name for pet in obj.tagged_pets.all())