from config.database import Base 
from sqlalchemy import Column, Integer, String, Text, Float, Enum

class Product(Base):
  __tablename__ = "products"

  productid = Column(Integer, primary_key=True, autoincrement=True)
  productname = Column(String(255), nullable=False)
  description = Column(Text)
  price = Column(Float, nullable=False)
  state = Column(Enum('Available', 'Unavailable'), default='Available', nullable=False)
