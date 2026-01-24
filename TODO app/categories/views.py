from django.shortcuts import render

from categories.models import Category


def list_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'list_categories.html', context=context)