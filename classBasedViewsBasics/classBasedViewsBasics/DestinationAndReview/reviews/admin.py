from django.contrib import admin

from destinations.models import Destination
from reviews.models import Review


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'created_at')
    prepopulated_fields = {'slug': ('name',)} # Автоматично попълва slug в админа

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'destination', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')