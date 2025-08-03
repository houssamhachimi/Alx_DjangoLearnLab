from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
]

from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns += [  # pyright: ignore[reportUndefinedVariable]
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from .views import login_view, logout_view, register_view

urlpatterns += [  # pyright: ignore[reportUndefinedVariable]
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
from .views import admin_view, librarian_view, member_view

urlpatterns += [  # pyright: ignore[reportUndefinedVariable]
    path('admin-area/', admin_view, name='admin_view'),
    path('librarian-area/', librarian_view, name='librarian_view'),
    path('member-area/', member_view, name='member_view'),
]
