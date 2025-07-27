from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),                    # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]

from django.urls import path, include

urlpatterns = [
    # other patterns...
    path('relationship/', include('relationship_app.urls')),
]
