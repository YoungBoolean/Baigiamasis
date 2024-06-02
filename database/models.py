from sqlalchemy import Column, Integer, String, Float, Date
from db import Base
from datetime import date


class User(Base):
    __tablename__ = "user_info"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    death_count = Column(Float)
    tipas = Column(String)

    def __init__(self, pavadinimas, suma, tipas, date=date.today()):
        self.pavadinimas = pavadinimas
        self.suma = suma
        self.tipas = tipas
        self.date = date

    def __str__(self):
        return f"{self.id}, {self.pavadinimas}, {self.suma}, {self.tipas}"


class Save(Base):
    __tablename__ = "user_saves"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    death_count = Column(Float)
    tipas = Column(String)

    def __init__(self, pavadinimas, suma, tipas, date=date.today()):
        self.pavadinimas = pavadinimas
        self.suma = suma
        self.tipas = tipas
        self.date = date

    def __str__(self):
        return f"{self.id}, {self.pavadinimas}, {self.suma}, {self.tipas}"

