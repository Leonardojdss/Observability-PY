from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, ConfigDict, EmailStr
from sqlalchemy.ext.declarative import declarative_base

class UserModel(declarative_base()):
    """
    Class representing a table "Users" in the database.
    """
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)