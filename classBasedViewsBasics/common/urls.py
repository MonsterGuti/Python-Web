from django.urls import path

from common import views

app_name = 'common'

urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('age-check/', views.AgeCheckRedirectView.as_view(), name='age-check'),
    path('teen/', views.HomeTeenWelcomeView.as_view(), name='home-teen'),
]
