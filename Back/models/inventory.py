'''
  Developed by Brayan Cataño Giraldo.
  E-mail: b.catano@utp.edu.co
'''

'''
  This file contains the Inventory model.
  It is used to map the Inventory model with the database table.
'''
# Import libraries and functions
from config.database import Base 
from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint, Enum

# Create the Inventory class model
class Inventory(Base):
  __tablename__ = "inventory"

  inventoryid = Column(Integer, primary_key=True, autoincrement=True)
  idflowershops = Column(Integer, ForeignKey('flowershops.idflowershops'), nullable=False)
  productid = Column(Integer, ForeignKey('products.productid'), nullable=False)
  quantity = Column(Integer, CheckConstraint('quantity > 0'), nullable=False)
  providerid = Column(Integer, ForeignKey('providers.providerid'), nullable=False)
  state = Column(Enum('Activate', 'Inactive'), default='Activate', nullable=False)
