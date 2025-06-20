# 📚 BookHexAPI

**BookHexAPI** is a clean, modular Book Management API built with FastAPI using the **Hexagonal Architecture (Ports and Adapters)** pattern. It serves as a practical implementation of clean architecture principles with a focus on maintainability, separation of concerns, and testability.

---

## 🚀 Features

- ✅ CRUD operations for books
- ✅ Domain-driven architecture
- ✅ PostgreSQL + SQLAlchemy for persistence
- ✅ FastAPI for building a modern REST API
- ✅ Pydantic for request/response validation
- ✅ Alembic for database migrations
- ✅ Clear separation between domain, application, and infrastructure layers
- ✅ Dockerized for easy development and deployment

---

## 🧱 Architecture Overview

```
book_hex_api/
├── app/
│   ├── domain/           # Business logic & interfaces
│   ├── application/      # Use cases and services
│   ├── infrastructure/   # DB adapters & API routes
│   └── main.py           # FastAPI entry point
├── tests/                # Unit & integration tests
├── alembic/              # Database migrations
├── docker-compose.yml    # Docker orchestration
├── Dockerfile            # FastAPI container
├── requirements.txt
└── .env
```

---

## 💡 Project Goals

This project aims to:

- Practice Hexagonal Architecture in Python
- Decouple business logic from infrastructure
- Build scalable and testable APIs
- Serve as a reference or boilerplate for future APIs

---

## 🛠️ Tech Stack

- **FastAPI** – High-performance web framework
- **SQLAlchemy** – ORM for Python
- **PostgreSQL** – Relational database
- **Pydantic** – Data validation and parsing
- **Alembic** – Database migrations
- **Docker** – Containerized development and deployment

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/book-hexagonal-api.git
cd book-hexagonal-api
```

### 2. Create `.env` file

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/bookdb
```

### 3. Run the application using Docker

```bash
docker-compose up --build
```

The API will be available at: `http://localhost:8000`

Access the interactive docs at: `http://localhost:8000/docs`

---

## 📌 License

This project is licensed under the MIT License.

---

## 🙌 Contributing

Feel free to fork this repo and submit pull requests. Suggestions and improvements are welcome!

