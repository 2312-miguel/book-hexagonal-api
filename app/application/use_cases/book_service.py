from typing import List, Optional
from app.domain.book import Book
from app.domain.ports.book_repository import BookRepository

class BookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def create_book(self, title: str, author: str, isbn: str) -> Book:
        new_book = Book(title=title, author=author, isbn=isbn)
        return self.book_repository.save(new_book)

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return self.book_repository.get_by_id(book_id)

    def get_all_books(self) -> List[Book]:
        return self.book_repository.get_all()

    def delete_book(self, book_id: int) -> None:
        return self.book_repository.delete_by_id(book_id) 