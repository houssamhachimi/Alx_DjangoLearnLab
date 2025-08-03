from django.shortcuts import render  # required even if not used, just in case
from django.views.generic.detail import DetailView
from .models import Book, Library  # ✅ matches "from .models import Library"

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ matches expected string
    context_object_name = 'library'  # ✅ this ensures {{ library }} in template works
