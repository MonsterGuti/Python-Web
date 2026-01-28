from django.db.models import Avg
from django.shortcuts import render, get_object_or_404

from books.models import Book


def landing_page(request):
    total_books = Book.objects.all().count()
    latest_book = Book.objects.order_by('-publishing_date').first()

    context = {
        'total_books': total_books,
        'latest_book': latest_book,
        'page_title': 'Landing Page'
    }

    return render(request, 'books/landing_page.html', context)


def book_list(request):
    books = Book.objects.annotate(
        avg_rating=Avg('reviews__rating'),
    ).order_by('title')

    context = {
        'books': books,
        'page_title': 'Book List'
    }

    return render(request, 'books/list.html', context)


def book_detail(request, slug):
    book = get_object_or_404(
        Book.objects.annotate(
            avg_rating=Avg('reviews__rating'),
        ),
        slug=slug,
    )

    context = {
        'book': book,
        'page_title': f'{book.title} details',
    }

    return render(request, 'books/detail.html', context)


