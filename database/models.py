"""
models.py

This module contains the SQLalchemy imports, and defines sqlalchemy database models.
"""

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import date

Base = declarative_base()


class SaveFile(Base):
    """SaveFile class, to be used as a database model"""
    __tablename__ = "save_file"
    id = Column(Integer, primary_key=True)
    game_stage = Column(String)
    date = Column(Date, default=date.today())
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates='save_files')


class User(Base):
    """User class, to be used as a database model"""
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    save_files = relationship("SaveFile", back_populates="user", cascade="all")
