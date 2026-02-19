from django.contrib import admin

from books import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'price']