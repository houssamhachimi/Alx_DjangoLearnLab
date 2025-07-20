# Deleting a Book

To delete the book titled "1984":

```python
book = Book.objects.get(title="1984")
book.delete()
