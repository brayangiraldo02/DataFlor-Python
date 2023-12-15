'''
  Developed by Brayan Cataño Giraldo.
  E-mail: b.catano@utp.edu.co
'''

'''
  This file contains the FlowerShop model.
  It is used to map the FlowerShop model with the database table.
'''

# Import libraries and functions
from config.database import Base
from sqlalchemy import Column, Integer, String, Enum

# Create the FlowerShop class model
class FlowerShop(Base):
  __tablename__ = "flowershops"

  idflowershops = Column(Integer, primary_key=True, autoincrement=True)
  fullname = Column(String(255), nullable=False)
  address = Column(String, nullable=False)
  phone = Column(String(15), nullable=False)
  state = Column(Enum('Activate', 'Inactive'), default='Activate', nullable=False)
