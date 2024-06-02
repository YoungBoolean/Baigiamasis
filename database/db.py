from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models import User

engine = create_engine("sqlite:///user_database.db")
Base = declarative_base()

Base.metadata.create_all(engine)