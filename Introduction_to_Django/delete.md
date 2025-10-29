
### 📝 **delete.md**

# Delete Operation (Book Model)

## Python Command
```python
from bookshelf.models import Book

# Retrieve the record to delete
book = Book.objects.get(id=1)

# Delete the record
book.delete()
```

### Output

```python
(1, {'bookshelf.Book': 1})
```


### Description

- Deletes the book record with id=1 from the database.

- The return value `(1, {'bookshelf.Book': 1})` shows one record deleted from the Book table.

To delete multiple records:

```python
Book.objects.filter(author="J.K. Rowling").delete()
```