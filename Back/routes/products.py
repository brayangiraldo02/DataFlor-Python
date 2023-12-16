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
from models.products import Product as ProductsModel
from fastapi.encoders import jsonable_encoder
from schemas.products import Product, ProductUpdate, ProductCreate

# Create the products router
products_router = APIRouter()

@products_router.get("/products", tags=["Products"], response_model=List[Product], status_code=200)
def get_products() -> List[Product]:
  db = Session()
  result = db.query(ProductsModel).all()
  response = JSONResponse(status_code=200, content=jsonable_encoder(result))
  if not result:
    response = JSONResponse(status_code=404, content={"message": "No products found."})
  return response

@products_router.get("/products/{productid}", tags=["Products"], response_model=Product, status_code=200)
def get_product(productid:int = Path(ge=0, le=2000)):
  db = Session()
  result = db.query(ProductsModel).filter(ProductsModel.productid == productid).first()
  response = JSONResponse(content=jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message": "No product found with that id"}, status_code=404)
  return response

@products_router.get("/products/name/{productname}", tags=["Products"], response_model=List[Product], status_code=200)
def get_productByName(productname:str = Path(min_length=1, max_length=255)):
  db = Session()
  result = db.query(ProductsModel).filter(ProductsModel.productname == productname).all()
  response = JSONResponse(content= jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message":"No product found with that name"}, status_code=404)
  return response

@products_router.post("/products/create", tags=["Products"], response_model=dict, status_code=201)
def create_product(product: ProductCreate):
  db = Session()
  newProduct = ProductsModel(productname=product.productname, description=product.description, price=product.price)
  db.add(newProduct)
  db.commit()
  response = JSONResponse(content={"message": "Product created successfully"}, status_code=201)
  return response

@products_router.put("/products/update/id/{productid}", tags=["Products"], response_model=dict, status_code=200)
def update_product(productid:int, product:ProductUpdate):
  db = Session()
  result = db.query(ProductsModel).filter(ProductsModel.productid == productid).first()
  if result:
    result.productname = product.productname
    result.description = product.description
    result.price = product.price
    result.state = product.state
    db.commit()
    response = JSONResponse(content={"message": "Product updated successfully"}, status_code=200)
  else:
    response = JSONResponse(content={"message": "No product found with that id"}, status_code=404)
  return response