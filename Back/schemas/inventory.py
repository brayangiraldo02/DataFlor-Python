'''
  Developed by Brayan Cataño Giraldo.
  E-mail: b.catano@utp.edu.co
'''

'''
  This file contains the Inventory schema.
  It is used to validate the Inventory data.
'''
# Importing libraries
from pydantic import BaseModel, Field, constr
from enum import Enum

# States for Inventory
class InventoryState(str, Enum):
  Activate = "Activate"
  Inactive = "Inactive"

# Inventory create
class InventoryCreate(BaseModel):
  idflowershops: int
  productid: int
  providerid: int
  quantity: int

# Inventory Base
class Inventory(BaseModel):
  inventoryid: int
  idflowershops: int
  productid: int
  providerid: int
  quantity: int
  state: InventoryState

# Inventory All
class InventoryAll(BaseModel):
  inventoryid: int
  flowerShopName: str
  productName: str
  providerName: str
  quantity: int
  priceProduct: int
  priceQuantity: int
  state: InventoryState

# Inventory Update
class InventoryUpdate(BaseModel):
  productid: int
  quantity: int
  state: InventoryState