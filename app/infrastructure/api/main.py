from fastapi import FastAPI
from app.infrastructure.database.database import Base, engine
from app.infrastructure.api.routers import books

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(books.router, prefix="/books", tags=["books"])

@app.get("/")
def read_root():
    return {"message": "API de Libros - Arquitectura Hexagonal"}