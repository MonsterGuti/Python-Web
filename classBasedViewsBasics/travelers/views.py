from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.views.generic import ListView

from reviews.mixins import RecentObjectMixin
from .models import Traveler


from travelers.forms import TravelForm
from travelers.models import Traveler


class TravelerCreateView(CreateView):
    model = Traveler
    fields = ['name', 'email', 'age', 'country']
    success_url = reverse_lazy('common:home')

    def form_valid(self, form):
        messages.success(self.request, 'Traveler Created')
        return super().form_valid(form)


class TravelerUpdateView(UpdateView):
    model = Traveler
    form_class = TravelForm
    success_url = reverse_lazy('common:home')


class TravelerDeleteView(DeleteView):
    model = Traveler
    success_url = reverse_lazy('common:home')


class TravelerDetailView(DetailView):
    model = Traveler

    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['reviews_count'] = self.object.reviews.count()
        return context


class TravelerListView(ListView, RecentObjectMixin):
    model = Traveler
    paginate_by = 1
    ordering = ['-name']
    context_object_name = 'travelers'
    recent_results_limit = 2

    def get_queryset(self):
        qs = Traveler.objects.filter(age__gte=21)

        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(name__icontains=query)

        return qs

