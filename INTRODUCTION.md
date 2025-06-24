# INTRODUCTION

## Project Objective

The purpose of this project was to build a Book Management API applying the **Hexagonal Architecture (Ports and Adapters)**, aiming for a decoupled, maintainable, and easily testable system.

---

## Process and Key Decisions

### 1. Architecture Definition
- Hexagonal architecture was chosen to clearly separate business logic (domain), use cases (application), and infrastructure (data access, API, etc.).
- Ports (interfaces) and adapters were designed to allow easy replacement of technologies or frameworks.

### 2. Project Structure
- The folder structure was created: `domain`, `application`, `infrastructure`, following the hexagonal pattern.
- Entities and ports were implemented in the domain layer.
- Use cases and services were placed in the application layer.
- Database adapters and API routers were implemented in the infrastructure layer.

### 3. Technology Choices
- **FastAPI** for building the REST API.
- **SQLAlchemy** as the ORM for data persistence.
- **PostgreSQL** as the relational database.
- **Pydantic** for data validation.
- **Alembic** for database migrations.
- **Docker** for containerization and easy deployment.

### 4. API Implementation
- The main entry point was created in `main.py`.
- The books router was developed to expose CRUD operations.
- The API was connected to the application and domain layers through ports and adapters.

### 5. Persistence and Database
- Database models were defined using SQLAlchemy.
- The book repository was implemented as a persistence adapter.
- Connection to PostgreSQL and migrations with Alembic were configured.

### 6. Testing and Validation
- The structure for unit and integration tests was prepared.
- Endpoints and integration between layers were validated.

### 7. Containerization and Deployment
- A `Dockerfile` was created for the application and a `docker-compose.yml` to orchestrate the database and API.
- The deployment and usage process was documented in the README.

---

## Main Commands Used to Create and Run the Project with Docker Only

### 1. Create the `.env` file
- Create a `.env` file with:
```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/bookdb
POSTGRES_DB=books_db
POSTGRES_USER=books_user
POSTGRES_PASSWORD=books_password
```

### 2. Build and run the application with Docker Compose
```bash
docker-compose up --build
```

### 3. Alembic database migrations with Docker
- To generate a new migration:
```bash
docker-compose run --rm api alembic revision --autogenerate -m "Migration message"
```
- To apply migrations:
```bash
docker-compose run --rm api alembic upgrade head
```

### 4. Access the API
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs

---

## Result

The result is a modular, decoupled API ready to scale or adapt to new technologies, serving as a reference for future projects based on hexagonal architecture.

---

## Final Notes

This project is a practical example of how to apply hexagonal architecture in Python, making the system maintainable and easy to evolve over time. 