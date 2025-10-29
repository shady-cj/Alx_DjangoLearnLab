### 📝 **update.md**
```markdown
# Update Operation (Book Model)

## Python Command
```python
from bookshelf.models import Book

# Retrieve the book to update
book = Book.objects.get(id=1)

# Modify its attributes
book.title = "Nineteen Eight-Four"

# Save changes to the database
book.save()
```


### Description

The above commands:

- Retrieve a book by id

- Change its publication_year and title

- Persist the new data using .save()