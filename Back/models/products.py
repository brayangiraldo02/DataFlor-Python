'''
  Developed by Brayan Cataño Giraldo.
  E-mail: b.catano@utp.edu.co
'''

'''
  This file contains the Product model.
  It is used to map the Product model with the database table.
'''
# Import libraries and functions
from config.database import Base 
from sqlalchemy import Column, Integer, String, Text, Float, Enum

# Create the Product class model
class Product(Base):
  __tablename__ = "products"

  productid = Column(Integer, primary_key=True, autoincrement=True)
  productname = Column(String(255), nullable=False)
  description = Column(Text)
  price = Column(Float, nullable=False)
  state = Column(Enum('Activate', 'Inactive'), default='Activate', nullable=False)
