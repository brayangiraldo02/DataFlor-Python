'''
  Developed by Brayan Cataño Giraldo.
  E-mail: b.catano@utp.edu.co
'''

'''
  This file contains the Product schema.
  It is used to validate the Product data.
'''
# Importing libraries
from pydantic import BaseModel, Field, constr
from enum import Enum

# Product State
class ProductState(str, Enum):
  Activate = "Activate"
  Inactive = "Inactive"

# Product Base
class Product(BaseModel):
  productid: int
  productname: constr(min_length=1, max_length=255)
  description: constr(min_length=1, max_length=255)
  price: float
  state: ProductState

# Product Update
class ProductUpdate(BaseModel):
  productname: constr(min_length=1, max_length=255)
  description: constr(min_length=1, max_length=255)
  price: float
  state: ProductState

# Product Create
class ProductCreate(BaseModel):
  productname: constr(min_length=1, max_length=255)
  description: constr(min_length=1, max_length=255)
  price: float