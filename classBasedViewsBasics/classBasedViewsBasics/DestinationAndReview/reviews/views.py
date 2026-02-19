from django.shortcuts import render, get_object_or_404

from destinations.models import Destination
from reviews.models import Review

DEFAULT_REVIEW_COUNT = 5

def recent_reviews(request):
    review_count = request.GET.get('review_count', DEFAULT_REVIEW_COUNT)
    reviews = Review.objects.filter(is_published=True).order_by('-created_at')[:int(review_count)]

    context = {
        'review_count': review_count,
        'reviews': reviews,
        'title': 'Recent Reviews',
    }

    return render(request, 'review/list.html', context)

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)

    context = {
        'review': review,
        'title': f'{review.author}\'s Review on {review.destination.name}',
    }

    return render(request, 'review/detail.html', context)

def reviews_by_year(request, year):
    reviews = Review.objects.filter(created_at__year=year)

    context = {
        'reviews': reviews,
        'title': f'Reviews by {year}',
    }

    return render(request, 'review/list.html', context)