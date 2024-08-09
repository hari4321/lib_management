from django.urls import path
from .views import (
    retrieve_member, add_member,
    retrieve_author, add_author,
    retrieve_book, add_book,
    retrieve_borrowed_books, add_borrowed_books
)

urlpatterns = [
    path('members/<int:mem_id>/', retrieve_member, name='retrieve-member'),
    path('members/add/', add_member, name='add-member'),
    path('authors/<int:author_id>/', retrieve_author, name='retrieve-author'),
    path('authors/add/', add_author, name='add-author'),
    path('books/<int:book_id>/', retrieve_book, name='retrieve-book'),
    path('books/add/', add_book, name='add-book'),
    path('borrowed-books/<int:pk>/', retrieve_borrowed_books, name='retrieve-borrowed-book'),
    path('borrowed-books/add/', add_borrowed_books, name='add-borrowed-book'),
]
