'''
  Developed by Brayan Cataño Giraldo.
  E-mail: b.catano@utp.edu.co
'''

'''
  This file contains the providers routes.
'''
# Import libraries and functions
from fastapi import APIRouter, Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.providers import Provider as ProvidersModel
from fastapi.encoders import jsonable_encoder
from schemas.providers import Providers, ProvidersUpdate

# Create the providers router
providers_router = APIRouter()

# Get all providers
@providers_router.get("/providers", tags=["Providers"], response_model=List[Providers], status_code=200)
def get_providers() -> List[Providers]:
  db = Session()
  result = db.query(ProvidersModel).all()
  response = JSONResponse(status_code=200, content=jsonable_encoder(result))
  if not result:
    response = JSONResponse(status_code=404, content={"message": "No providers found."})
  return response

# Get provider by id
@providers_router.get("/providers/{providerid}", tags=["Providers"], response_model=Providers, status_code=200)
def get_providers(providerid:int = Path(ge=0, le=2000)):
  db = Session()
  result = db.query(ProvidersModel).filter(ProvidersModel.providerid == providerid).first()
  response = JSONResponse(content=jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message": "No provider found with that id"}, status_code=404)
  return response

# Get provider by name
@providers_router.get("/providers/name/{fullname}", tags=["Providers"], response_model=List[Providers], status_code=200)
def get_providerByName(fullname:str = Path(min_length=1, max_length=255)):
  db = Session()
  result = db.query(ProvidersModel).filter(ProvidersModel.fullname == fullname).all()
  response = JSONResponse(content= jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message":"No providers found with that name"}, status_code=404)
  return response

# Get provider by address
@providers_router.get("/providers/address/{address}", tags=["Providers"], response_model=List[Providers], status_code=200)
def get_providerByAddress(address:str = Path(min_length=1, max_length=255)):
  db = Session()
  result = db.query(ProvidersModel).filter(ProvidersModel.address == address).all()
  response = JSONResponse(content= jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message":"No provider found with that address"}, status_code=404)
  return response

# Get provider by phone
@providers_router.get("/providers/phone/{phone}", tags=["Providers"], response_model=List[Providers], status_code=200)
def get_providerByPhone(phone:str = Path(min_length=1, max_length=255)):
  db = Session()
  result = db.query(ProvidersModel).filter(ProvidersModel.phone == phone).all()
  response = JSONResponse(content= jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message":"No provider found with that phone"}, status_code=404)
  return response

# Get provider by state
@providers_router.get("/providers/state/{state}", tags=["Providers"], response_model=List[Providers], status_code=200)
def get_providerByState(state:str = Path(min_length=1, max_length=255)):
  db = Session()
  result = db.query(ProvidersModel).filter(ProvidersModel.state == state).all()
  response = JSONResponse(content= jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message":"No provider found with that state"}, status_code=404)
  return response

# Create provider
@providers_router.post("/providers/create", tags=["Providers"], response_model=dict, status_code=201)
def create_flowerShop(Providers: Providers):
  db = Session()
  new_provider = ProvidersModel(**Providers.model_dump())
  db.add(new_provider)
  db.commit()
  return JSONResponse(status_code=201, content={"message": "provider created"})

# Update provider by id
@providers_router.put("/providers/update/id/{providerid}", tags=["Providers"], status_code=200)
def update_flowerShopById(providerid:int, Provider: ProvidersUpdate):
  db = Session()
  result = db.query(ProvidersModel).filter(ProvidersModel.providerid == providerid).first()
  if not result:
    return JSONResponse(status_code=404, content={"message": "No provider found with that id"})
  result.fullname = Provider.fullname
  result.address = Provider.address
  result.phone = Provider.phone
  result.state = Provider.state
  db.commit()
  return JSONResponse(status_code=200, content={"message": "provider updated"})

# Update provider by fullname
@providers_router.put("/providers/update/fullname/{fullname}", tags=["Providers"], status_code=200)
def update_user(fullname: str, Provider: ProvidersUpdate):
  db = Session()
  result = db.query(ProvidersModel).filter(ProvidersModel.fullname == fullname).first()
  if not result:
    return JSONResponse(status_code=404, content={"message": "Provider not found"})
  result.fullname = Provider.fullname
  result.address = Provider.address
  result.phone = Provider.phone
  result.state = Provider.state
  db.commit()
  return JSONResponse(status_code=200, content={"message": "Provider updated successfully"})