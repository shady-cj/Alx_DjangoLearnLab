### 📝 **retrieve.md**
```markdown
# Retrieve Operation (Book Model)

## Python Command
```python
from bookshelf.models import Book

# Retrieve a single record by its ID
book = Book.objects.get(title="1984")
book

# Retrieve all books
books = Book.objects.all()
books
```

### Output

```python
<Book: 1984 (1949)>
<QuerySet [<Book: 1984 (1949)>]>
```


### Description

- `Book.objects.get(id=1)` fetches one record where `id=1`.

- `Book.objects.all()` returns all book records as a `QuerySet`.

You can also use filters:

```python
Book.objects.filter(author="J.K. Rowling")
```