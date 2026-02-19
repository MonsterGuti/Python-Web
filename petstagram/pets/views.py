from django.db.models import Prefetch
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

import accounts
from pets.forms import PetForm
from pets.models import Pet


class PetCreateView(CreateView):
    template_name = 'pets/pet-add-page.html'
    model = Pet
    form_class = PetForm
    success_url = reverse_lazy('accounts:details', kwargs={'pk': 1})


# def pet_add(request: HttpRequest) -> HttpResponse:
#     form = PetForm(request.POST or None)
#
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return redirect('accounts:details', pk=1)
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'pets/pet-add-page.html', context)
#

from django.db.models import Prefetch
from photos.models import Photo


class PetDetailView(DetailView):
    template_name = 'pets/pet-details-page.html'
    queryset = Pet.objects.prefetch_related(
        Prefetch(
            'photos',
            queryset=Photo.objects.prefetch_related('tagged_pets'),
        )
    )
    slug_url_kwarg = 'pet_slug'


# def pet_details(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
#     pet = Pet.objects.prefetch_related(
#         Prefetch(
#             'photos',
#             queryset=Photo.objects.prefetch_related('tagged_pets'),
#         )
#     ).get(slug=pet_slug)
#
#     context = {
#         'pet': pet,
#     }
#
#     return render(request, 'pets/pet-details-page.html', context)


class PetEditView(UpdateView):
    template_name = 'pets/pet-edit-page.html'
    model = Pet
    form_class = PetForm
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse('pets:details',
                       kwargs={
                           'username': 'username', 'pet_slug': self.object.slug
                       })


# def pet_edit(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
#     pet = Pet.objects.get(slug=pet_slug)
#     form = PetForm(request.POST or None, instance=pet)
#
#     if request.method == "POST" and form.is_valid():
#         instance = form.save()
#         return redirect('pets:details', username=username, pet_slug=instance.slug)
#
#     context = {
#         'form': form,
#         'pet': pet,
#     }
#
#     return render(request, 'pets/pet-edit-page.html', context)


class PetDeleteView(DeleteView):
    template_name = 'pets/pet-delete-page.html'
    model = Pet
    success_url = reverse_lazy('accounts:details', kwargs={'pk': 1})

    slug_field = 'slug'
    slug_url_kwarg = 'pet_slug'

    def get_initial(self):
        return self.object.__dict__



# def pet_delete(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
#     pet = Pet.objects.get(slug=pet_slug)
#     form = PetForm(request.POST or None, instance=pet)
#
#     if request.method == "POST" and form.is_valid():
#         pet.delete()
#         return redirect('accounts:details', pk=1)
#
#     context = {
#         'form': form,
#         'pet': pet,
#     }
#
#     return render(request, 'pets/pet-delete-page.html', context)
