# Create Operation (Book Model)

## Python Command
```python
from bookshelf.models import Book

# Create a new Book record
book = Book.objects.create(
    title="Down and Out in Paris and London ",
    author="George orwell",
    publication_year=2024
)

```

### Output
```python
<Book: Harry Potter by J.K. Rowling (2024)>
1
```

### Description

This creates and saves a new Book record in the database with:

- Title: Harry Potter

- Author: J.K. Rowling

- Publication Year: 2024

- Auto-assigned ID: 1