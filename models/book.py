from config.database import Base
from sqlalchemy import Column, Integer, String

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    autor = Column(String)
    year = Column(Integer)
    category = Column(String)
    pages = Column(Integer)

