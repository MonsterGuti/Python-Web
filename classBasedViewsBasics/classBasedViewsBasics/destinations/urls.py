from django.urls import path

from destinations import views

urlpatterns = [
    path('create/', views.DestinationCreateView.as_view(), name='destination-create'),
]