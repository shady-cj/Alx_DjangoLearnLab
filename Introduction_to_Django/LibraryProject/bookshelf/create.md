# Create Operation (Book Model)

## Python Command
```python
from bookshelf.models import Book

# Create a new Book record
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

```

### Output
```python
<Book: 1984 (1949)>
1
```

### Description

This creates and saves a new Book record in the database with:

- Title: Harry Potter

- Author: J.K. Rowling

- Publication Year: 2024

- Auto-assigned ID: 1