from django.urls import path

from reviews.views import (
    recent_reviews,
    review_details,
    review_create,
    review_edit,
    review_delete,
)

app_name = 'reviews'

urlpatterns = [
    path('', recent_reviews, name='list'),        # <-- MAIN
    path('recent/', recent_reviews, name='recent'),  # <-- optional
    path('create/', review_create, name='create'),
    path('<int:pk>/', review_details, name='details'),
    path('<int:pk>/edit/', review_edit, name='edit'),
    path('<int:pk>/delete/', review_delete, name='delete'),
]
