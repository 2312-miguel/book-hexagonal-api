from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.book import Book as DomainBook
from app.domain.ports.book_repository import BookRepository
from app.infrastructure.database.models import Book as DBBook

class SQLAlchemyBookRepository(BookRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def save(self, book: DomainBook) -> DomainBook:
        db_book = DBBook(title=book.title, author=book.author, isbn=book.isbn)
        if book.id:
            db_book = self.db_session.query(DBBook).filter(DBBook.id == book.id).first()
            if db_book:
                db_book.title = book.title
                db_book.author = book.author
                db_book.isbn = book.isbn
        else:
            self.db_session.add(db_book)
        
        self.db_session.commit()
        self.db_session.refresh(db_book)
        return DomainBook.from_orm(db_book)

    def get_by_id(self, book_id: int) -> Optional[DomainBook]:
        db_book = self.db_session.query(DBBook).filter(DBBook.id == book_id).first()
        if db_book:
            return DomainBook.from_orm(db_book)
        return None

    def get_all(self) -> List[DomainBook]:
        all_db_books = self.db_session.query(DBBook).all()
        return [DomainBook.from_orm(db_book) for db_book in all_db_books]

    def delete_by_id(self, book_id: int) -> None:
        db_book = self.db_session.query(DBBook).filter(DBBook.id == book_id).first()
        if db_book:
            self.db_session.delete(db_book)
            self.db_session.commit() 