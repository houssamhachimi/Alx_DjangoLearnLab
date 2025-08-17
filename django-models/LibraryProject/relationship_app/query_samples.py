import os
import sys
import django

# Add project root (where manage.py lives) to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# Setup Django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Query all books by a specific author
    try:
        author = Author.objects.get(name="Jane Austen")
        books_by_author = Book.objects.filter(author=author)
        print(f"\nBooks by {author.name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print("\nAuthor 'Jane Austen' not found.")

    # Query all books in a library
    library = None
    try:
        library = Library.objects.get(name="Central Library")
        books_in_library = library.books.all()
        print(f"\nBooks in {library.name}:")
        for book in books_in_library:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print("\nLibrary 'Central Library' not found.")

    # Retrieve the librarian for the library (only if library exists)
    if library is not None:
        try:
            librarian = Librarian.objects.get(library=library)
            print(f"\nLibrarian of {library.name}: {librarian.name}")
        except Librarian.DoesNotExist:
            print(f"\nNo librarian assigned to {library.name}.")

if __name__ == "__main__":
    run_queries()
