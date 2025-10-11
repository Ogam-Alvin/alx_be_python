# library_system.py

# Base Class
class Book:
    def __init__(self, title, author):
        """Initialize the title and author of a book"""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for a generic book"""
        return f"Book: {self.title} by {self.author}"


# Derived Class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook with title, author, and file size"""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation for an eBook"""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with title, author, and page count"""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation for a print book"""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition Class: Library
class Library:
    def __init__(self):
        """Initialize an empty list of books"""
        self.books = []

    def add_book(self, book):
        """Add a book instance to the library collection"""
        self.books.append(book)

    def list_books(self):
        """List all books currently in the library"""
        for book in self.books:
            print(book)
