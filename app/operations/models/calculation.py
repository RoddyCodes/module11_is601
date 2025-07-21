# app/models/calculation.py
from datetime import datetime
import uuid
from typing import List
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.operations.database import Base

class User(Base):
    __tablename__ = "users"
    # Basic User model for the foreign key relationship
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    # ... other user fields
    
    calculations = relationship("Calculation", back_populates="owner")


class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    a = Column(Float, nullable=False)
    b = Column(Float, nullable=False)
    operation_type = Column(String, nullable=False)
    result = Column(Float, nullable=False)
    
    # Correctly implemented foreign key to the users table
    user_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="calculations")