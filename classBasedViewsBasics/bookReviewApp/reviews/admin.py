from django.contrib import admin

from reviews import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book__title', 'rating']