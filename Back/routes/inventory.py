'''
  Developed by Brayan Cataño Giraldo.
  E-mail: b.catano@utp.edu.co
'''

'''
  This file contains the products routes.
'''
# Import libraries and functions
from fastapi import APIRouter, Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.inventory import Inventory as InventoryModel
from models.flowershops import FlowerShop as FlowerShopModel
from models.products import Product as ProductModel
from models.providers import Provider as ProviderModel
from fastapi.encoders import jsonable_encoder
from schemas.inventory import Inventory, InventoryCreate, InventoryUpdate, InventoryAll
from sqlalchemy.orm import joinedload

# Create the inventory router
inventory_router = APIRouter()

# Get all inventory
@inventory_router.get("/inventory", tags=["Inventory"], response_model=List[InventoryAll], status_code=200)
def get_inventory() -> List[InventoryAll]:
  db = Session()
  result = (
    db.query(
      InventoryModel.inventoryid,
      InventoryModel.idflowershops,
      FlowerShopModel.fullname.label("flowerShopName"),
      InventoryModel.productid,
      ProductModel.productname.label("productName"),
      ProductModel.price,
      InventoryModel.quantity,
      InventoryModel.providerid,
      ProviderModel.fullname.label("providerName"),
      InventoryModel.state,
    )
    .join(FlowerShopModel, InventoryModel.idflowershops == FlowerShopModel.idflowershops)
    .join(ProductModel, InventoryModel.productid == ProductModel.productid)
    .join(ProviderModel, InventoryModel.providerid == ProviderModel.providerid)
    .all()
  )
  if not result:
    return JSONResponse(status_code=404, content={"message": "No inventory found."})

  inventory_list = [
    InventoryAll(
      inventoryid=row.inventoryid,
      flowerShopName=row.flowerShopName,
      productName=row.productName,
      providerName=row.providerName,
      quantity=row.quantity,
      priceProduct=row.price,
      priceQuantity=row.price * row.quantity,
      state=row.state
      )
      for row in result
  ]
  return inventory_list

# Get inventory by id
@inventory_router.get("/inventory/{idflowershops}", tags=["Inventory"], response_model=List[InventoryAll], status_code=200)
def get_inventory(idflowershops:int = Path(ge=0, le=2000)):
  db = Session()
  result = (
    db.query(
      InventoryModel.inventoryid,
      InventoryModel.idflowershops,
      FlowerShopModel.fullname.label("flowerShopName"),
      InventoryModel.productid,
      ProductModel.productname.label("productName"),
      ProductModel.price,
      InventoryModel.quantity,
      InventoryModel.providerid,
      ProviderModel.fullname.label("providerName"),
      InventoryModel.state,
    )
    .join(FlowerShopModel, InventoryModel.idflowershops == FlowerShopModel.idflowershops)
    .join(ProductModel, InventoryModel.productid == ProductModel.productid)
    .join(ProviderModel, InventoryModel.providerid == ProviderModel.providerid)
    .filter(InventoryModel.idflowershops == idflowershops)
    .all()
  )
  if not result:
    return JSONResponse(status_code=404, content={"message": "No inventory found."})

  inventory_list = [
    InventoryAll(
      inventoryid=row.inventoryid,
      flowerShopName=row.flowerShopName,
      productName=row.productName,
      providerName=row.providerName,
      quantity=row.quantity,
      priceProduct=row.price,
      priceQuantity=row.price * row.quantity,
      state=row.state
      )
      for row in result
  ]
  return inventory_list

# Post create inventory
@inventory_router.post("/inventory/create", tags=["Inventory"], response_model=dict, status_code=201)
def create_inventory(inventory: InventoryCreate):
  db = Session()
  newInventory = InventoryModel(idflowershops=inventory.idflowershops, productid=inventory.productid, providerid=inventory.providerid, quantity=inventory.quantity)
  db.add(newInventory)
  db.commit()
  response = JSONResponse(content={"message": "Inventory created successfully"}, status_code=201)
  return response

# Put update inventory
@inventory_router.put("/inventory/update/id/{inventoryid}", tags=["Inventory"], response_model=dict, status_code=200)
def update_inventory(inventoryid:int, inventory:InventoryAll):
  db = Session()
  result = db.query(InventoryModel).filter(InventoryModel.inventoryid == inventoryid).first()
  try:
    if result:
      # result.providerid = inventory.providerid
      result.quantity = inventory.quantity
      result.state = inventory.state
      db.commit()
      response = JSONResponse(content={"message": "Inventory updated successfully"}, status_code=200)
    else:
      response = JSONResponse(content={"message": "Inventory not found"}, status_code=404)
    return response
  except Exception as e:
    return JSONResponse(content={"message": f"Error: {str(e)}"}, status_code=500)