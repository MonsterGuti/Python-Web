from django.urls import path, re_path
from . import views
from .views import review_detail

app_name = 'review'
urlpatterns = [
    path('', views.recent_reviews, name='list'),
    re_path(r'^(?P<year>20\d{2})/$', views.reviews_by_year, name='reviews_by_year'),

    path('details/<int:pk>/', review_detail, name='detail'),
]