from django.urls import path
from destinations import views

app_name = 'destination'

urlpatterns = [
    path('', views.simple_view, name='simple_view'),
    path('redirect-home/', views.redirect_home, name='redirect_home'),
    path('destinations/', views.destination_list, name='list'),
    path('destinations/detail/<slug:slug>/', views.destination_detail, name='detail'),
]
