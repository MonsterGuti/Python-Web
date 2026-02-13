from tkinter.font import names

from django.urls import path, include

from books.views import landing_page, book_list, book_detail, book_create, book_edit, book_delete
from reviews.views import review_bulk_update

app_name = 'books'

books_patterns = [
    path('', book_list, name='list'),
    path('create/', book_create, name='create'),
    path('<slug:book_slug>/', review_bulk_update, name='update'),
    path('<int:pk>/', include([
        path('edit/', book_edit, name='edit'),
        path('delete/', book_delete, name='delete'),
    ])),
    path('<slug:slug>/', book_detail, name='details')
]
urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('books/', include(books_patterns)),
]
