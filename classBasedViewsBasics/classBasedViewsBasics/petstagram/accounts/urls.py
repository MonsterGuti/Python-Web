from django.urls import path, include

from accounts import views

app_name = 'accounts'

authentication_patterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]

profile_patterns = [
    path('', views.profile_details, name='details'),
    path('edit/', views.profile_edit, name='edit'),
    path('delete/', views.profile_delete, name='delete'),
]


urlpatterns = [
    path('', include(authentication_patterns)),
    path('profile/<int:pk>/', include(profile_patterns)),
]