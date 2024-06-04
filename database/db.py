"""
db.py

This module contains the SQLalchemy imports, engine, Session class.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

engine = create_engine("sqlite:///user_database.db")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
