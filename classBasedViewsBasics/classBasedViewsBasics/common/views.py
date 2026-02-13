from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils.timezone import now
from django.views import View
from django.views.generic import TemplateView, RedirectView

from travelers.models import Traveler


class WelcomeView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return HttpResponse('Welcome back!')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request) -> HttpResponse:
        return HttpResponse("Welcome to our travel app!")

    def post(self, request) -> HttpResponse:
        return HttpResponse("Post was called!")


class HomeView(TemplateView):
    def get_context_data(self, **kwargs):
        kwargs.update({
            'current_time': now(),
            'travelers_count': Traveler.objects.count(),
        })
        return super().get_context_data(**kwargs)

    def get_template_names(self):
        if self.request.user.is_staff:
            return ['admin_home.html']
        else:
            return ['home.html']


class HomeTeenWelcomeView(TemplateView):
    template_name = 'teen_welcome.html'


class AgeCheckRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        traveler = None
        pk = self.request.GET.get('pk')
        traveler = Traveler.objects.get(pk=pk)

        if traveler.age > 21:
            return reverse('common:home')
        else:
            return reverse('common:home-teen')
