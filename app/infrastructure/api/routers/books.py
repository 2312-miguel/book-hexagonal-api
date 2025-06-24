from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.domain.book import Book as DomainBook
from app.application.use_cases.book_service import BookService
from app.infrastructure.adapters.sqlalchemy_book_repository import SQLAlchemyBookRepository
from app.infrastructure.database.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_book_service(db: Session = Depends(get_db)) -> BookService:
    repository = SQLAlchemyBookRepository(db)
    return BookService(repository)

@router.post("/", response_model=DomainBook, status_code=201)
def create_book(book: DomainBook, service: BookService = Depends(get_book_service)):
    return service.create_book(book.title, book.author, book.isbn)

@router.get("/{book_id}", response_model=DomainBook)
def get_book(book_id: int, service: BookService = Depends(get_book_service)):
    book = service.get_book_by_id(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.get("/", response_model=List[DomainBook])
def get_all_books(service: BookService = Depends(get_book_service)):
    return service.get_all_books()

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, service: BookService = Depends(get_book_service)):
    service.delete_book(book_id)
    return 