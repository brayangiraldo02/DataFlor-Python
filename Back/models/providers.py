'''
  Developed by Brayan Cataño Giraldo.
  E-mail: b.catano@utp.edu.co
'''

'''
  This file contains the Provider model.
  It is used to map the Provider model with the database table.
'''
# Import libraries and functions
from config.database import Base 
from sqlalchemy import Column, Integer, String, Enum

# Create the Provider class model
class Provider(Base):
  __tablename__ = "providers"

  providerid = Column(Integer, primary_key=True, autoincrement=True)
  fullname = Column(String(255), nullable=False)
  phone = Column(String(15), nullable=False)
  address = Column(String, nullable=False)
  state = Column(Enum('Activate', 'Inactive'), default='Activate', nullable=False)
