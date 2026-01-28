
from django.urls import path, include

import reviews
from reviews.views import recent_reviews, review_details

app_name = 'reviews'

review_patterns = [
    path('recent/', recent_reviews, name='recent'),
    path('<int:pk>/', review_details, name='details'),
]
urlpatterns = [
    path('', include(review_patterns)),
]
