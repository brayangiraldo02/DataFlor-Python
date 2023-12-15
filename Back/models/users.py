'''
  Developed by Brayan Cataño Giraldo.
  E-mail: b.catano@utp.edu.co
'''

'''
  This file contains the User model.
  It is used to map the User model with the database table.
'''
# Import libraries and functions
from config.database import Base 
from sqlalchemy import Column, Integer, String, Enum, ForeignKey

# Create the User class model
class User(Base):
  __tablename__ = "users"

  userid = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String(50), nullable=False)
  password = Column(String(255), nullable=False)
  fullname = Column(String(255), nullable=False)
  phone = Column(String(15), nullable=False)
  role = Column(Enum('Admin', 'Dueño', 'Empleado'), nullable=False)
  idflowershops = Column(Integer, ForeignKey('flowershops.idflowershops'))
  state = Column(Enum('Activate', 'Inactive'), default='Activate', nullable=False)
