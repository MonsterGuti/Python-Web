import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from destinations.models import Destination
from reviews.models import Review


def simple_view(request):
    return HttpResponse("<h1>Hello, world. You're at the polls page.</h1>")


def destination_list(request):
    destinations = Destination.objects.all()

    context = {
        'destinations': destinations,
        'title': 'Destination List',
    }

    return render(request, 'destination/list.html', context)

def destination_detail(request, slug):
    destination = get_object_or_404(Destination, slug=slug)

    context = {
        'destination': destination,
        'title': f'{destination.name} Detail',
    }

    return render(request, 'destination/detail.html', context)

def redirect_home(request):
    return redirect('destination:list')