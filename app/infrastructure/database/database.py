import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Esta línea crea una clase base para el sistema declarativo de SQLAlchemy.
# Cualquier clase de modelo que definamos para representar una tabla en nuestra
# base de datos deberá heredar de esta clase `Base`.
Base = declarative_base()