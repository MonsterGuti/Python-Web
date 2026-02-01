from django.db.models import Avg, Q
from django.shortcuts import render, get_object_or_404, redirect

from books.forms import BookFormBasic, BookEditForm, BookDeleteForm, BookSearchForm
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
    search_form = BookSearchForm(request.GET or None)

    books = Book.objects.annotate(
        avg_rating=Avg('reviews__rating'),
    ).order_by('title')

    if 'query' in request.GET:
        if search_form.is_valid():
            searched_value = search_form.cleaned_data['query']
            books = books.filter(
                Q(title__icontains=searched_value) | Q(description__icontains=searched_value)
            )

    context = {
        'books': books,
        'page_title': 'Book List',
        'search_form': search_form,
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


def book_create(request):
    form = BookFormBasic(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('books:landing_page')

    context = {
        'form': form,
        'page_title': 'Add New Book',
    }

    return render(request, 'books/create.html', context)


def book_edit(request, pk: int):
    book = get_object_or_404(Book, pk=pk)
    form = BookEditForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('books:landing_page')

    context = {
        'form': form,
        'page_title': 'Add New Book',
    }

    return render(request, 'books/edit.html', context)


def book_delete(request, pk: int):
    book = get_object_or_404(Book, pk=pk)
    form = BookDeleteForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():
        book.delete()
        return redirect('books:landing_page')

    context = {
        'form': form,
        'page_title': 'Add New Book',
    }

    return render(request, 'books/delete.html', context)
