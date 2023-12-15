'''
  Developed by Brayan Cataño Giraldo.
  E-mail: b.catano@utp.edu.co
'''

'''
  This file contains the FlowerShop routes.
'''

# Import libraries and functions
from fastapi import APIRouter, Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.flowershops import FlowerShop as FlowerShopModel
from fastapi.encoders import jsonable_encoder
from schemas.flowershops import FlowerShop, FlowerShopUpdate

# Create the FlowerShop router
flowerShop_router = APIRouter()

# Get all flower shops
@flowerShop_router.get("/flower-shops", tags=["FlowerShops"], response_model=List[FlowerShop], status_code=200)
def get_flowerShops() -> List[FlowerShop]:
  db = Session()
  result = db.query(FlowerShopModel).all()
  response = JSONResponse(status_code=200, content=jsonable_encoder(result))
  if not result:
    response = JSONResponse(status_code=404, content={"message": "No flower shops found."})
  return response

# Get flower shop by id
@flowerShop_router.get("/flower-shops/{idflowershops}", tags=["FlowerShops"], response_model=FlowerShop, status_code=200)
def get_flowerShop(idflowershops:int = Path(ge=0, le=2000)):
  db = Session()
  result = db.query(FlowerShopModel).filter(FlowerShopModel.idflowershops == idflowershops).first()
  response = JSONResponse(content=jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message": "No flower shop found with that id"}, status_code=404)
  return response

# Get flower shop by name
@flowerShop_router.get("/flower-shops/name/{fullname}", tags=["FlowerShops"], response_model=List[FlowerShop], status_code=200)
def get_flowerShopByName(fullname:str = Path(min_length=1, max_length=255)):
  db = Session()
  result = db.query(FlowerShopModel).filter(FlowerShopModel.fullname == fullname).all()
  response = JSONResponse(content= jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message":"No flower shop found with that name"}, status_code=404)
  return response

# Get flower shop by address
@flowerShop_router.get("/flower-shops/address/{address}", tags=["FlowerShops"], response_model=List[FlowerShop], status_code=200)
def get_flowerShopByAddress(address:str = Path(min_length=1, max_length=255)):
  db = Session()
  result = db.query(FlowerShopModel).filter(FlowerShopModel.address == address).all()
  response = JSONResponse(content= jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message":"No flower shop found with that address"}, status_code=404)
  return response

# Get flower shop by phone
@flowerShop_router.get("/flower-shops/phone/{phone}", tags=["FlowerShops"], response_model=List[FlowerShop], status_code=200)
def get_flowerShopByPhone(phone:str = Path(min_length=1, max_length=255)):
  db = Session()
  result = db.query(FlowerShopModel).filter(FlowerShopModel.phone == phone).all()
  response = JSONResponse(content= jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message":"No flower shop found with that phone"}, status_code=404)
  return response

# Get flower shop by state
@flowerShop_router.get("/flower-shops/state/{state}", tags=["FlowerShops"], response_model=List[FlowerShop], status_code=200)
def get_flowerShopByState(state:str = Path(min_length=1, max_length=255)):
  db = Session()
  result = db.query(FlowerShopModel).filter(FlowerShopModel.state == state).all()
  response = JSONResponse(content= jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message":"No flower shop found with that state"}, status_code=404)
  return response

# Create flower shop
@flowerShop_router.post("/flower-shops/create", tags=["FlowerShops"], response_model=dict, status_code=201)
def create_flowerShop(flowerShop: FlowerShop):
  db = Session()
  new_flowerShop = FlowerShopModel(**flowerShop.model_dump())
  db.add(new_flowerShop)
  db.commit()
  return JSONResponse(status_code=201, content={"message": "Flower shop created"})

# Update flower shop by id
@flowerShop_router.put("/flower-shops/update/id/{idflowershops}", tags=["FlowerShops"], status_code=200)
def update_flowerShopById(idflowershops:int, flowerShop: FlowerShopUpdate):
  db = Session()
  result = db.query(FlowerShopModel).filter(FlowerShopModel.idflowershops == idflowershops).first()
  if not result:
    return JSONResponse(status_code=404, content={"message": "No flower shop found with that id"})
  result.fullname = flowerShop.fullname
  result.address = flowerShop.address
  result.phone = flowerShop.phone
  result.state = flowerShop.state
  db.commit()
  return JSONResponse(status_code=200, content={"message": "Flower shop updated"})

# Update flower shop by fullname
@flowerShop_router.put("/flower-shops/update/fullname/{fullname}", tags=["FlowerShops"], response_model=dict, status_code=200)
def update_flowerShopByFullname(fullname:str = Path(min_length=1, max_length=255), flowerShop: FlowerShopUpdate = Depends()):
  db = Session()
  result = db.query(FlowerShopModel).filter(FlowerShopModel.fullname == fullname).first()
  if not result:
    return JSONResponse(status_code=404, content={"message": "No flower shop found with that fullname"})
  db.query(FlowerShopModel).filter(FlowerShopModel.fullname == fullname).update(flowerShop.model_dump())
  db.commit()
  return JSONResponse(status_code=200, content={"message": "Flower shop updated"})