# Updating a Book

To update the title of the book "1984":

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
