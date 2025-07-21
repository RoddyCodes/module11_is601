# app/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Get the Database URL from environment variables
#    This is the "phone number" for your PostgreSQL server.
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/fastapi_db")

# 2. Create the SQLAlchemy engine
#    This is the main connection object.
engine = create_engine(DATABASE_URL)

# 3. Create a SessionLocal class
#    Each instance of a SessionLocal class will be a new database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Create a Base class
#    Your SQLAlchemy models in models.py will inherit from this class.
Base = declarative_base()