'''
  Developed by Brayan Cataño Giraldo.
  E-mail: b.catano@utp.edu.co
'''

'''
  This file contains the User routes
'''
# Import libraries and functions
from fastapi import APIRouter, Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.users import User as UserModel
from fastapi.encoders import jsonable_encoder
from schemas.users import User, UserUpdate, UserLogin
from utils.jwt_manager import create_token

# Create the User router
user_router = APIRouter()

# Get all users
@user_router.get("/users", tags=["Users"], response_model=List[User], status_code=200)
def get_users() -> List[User]:
  db = Session()
  result = db.query(UserModel).all()
  response = JSONResponse(status_code=200, content=jsonable_encoder(result))
  if not result:
    response = JSONResponse(status_code=404, content={"message": "No users found."})
  return response

# Get user by id
@user_router.get("/users/{userid}", tags=["Users"], response_model=User, status_code=200)
def get_user(userid:int = Path(ge=0, le=2000)):
  db = Session()
  result = db.query(UserModel).filter(UserModel.userid == userid).first()
  response = JSONResponse(content=jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message": "No user found with that id"}, status_code=404)
  return response

# Get user by username
@user_router.get("/users/username/{username}", tags=["Users"], response_model=List[User], status_code=200)
def get_userByUsername(username:str = Path(min_length=1, max_length=50)):
  db = Session()
  result = db.query(UserModel).filter(UserModel.username == username).all()
  response = JSONResponse(content= jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message":"No user found with that username"}, status_code=404)
  return response

# Get user by phone
@user_router.get("/users/phone/{phone}", tags=["Users"], response_model=List[User], status_code=200)
def get_userByPhone(phone:str = Path(min_length=1, max_length=15)):
  db = Session()
  result = db.query(UserModel).filter(UserModel.phone == phone).all()
  response = JSONResponse(content= jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message":"No user found with that phone"}, status_code=404)
  return response

# Get user by role
@user_router.get("/users/role/{role}", tags=["Users"], response_model=List[User], status_code=200)
def get_userByRole(role:str = Path(min_length=1, max_length=50)):
  db = Session()
  result = db.query(UserModel).filter(UserModel.role == role).all()
  response = JSONResponse(content= jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message":"No user found with that role"}, status_code=404)
  return response

# Get user by idflowerShops
@user_router.get("/users/idflowershops/{idflowershops}", tags=["Users"], response_model=List[User], status_code=200)
def get_userByIdflowerShops(idflowershops:int = Path(ge=0, le=2000)):
  db = Session()
  result = db.query(UserModel).filter(UserModel.idflowershops == idflowershops).all()
  response = JSONResponse(content= jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message":"No user found with that idflowerShops"}, status_code=404)
  return response

# Get user by state
@user_router.get("/users/state/{state}", tags=["Users"], response_model=List[User], status_code=200)
def get_userByState(state:str = Path(min_length=1, max_length=50)):
  db = Session()
  result = db.query(UserModel).filter(UserModel.state == state).all()
  response = JSONResponse(content= jsonable_encoder(result), status_code=200)
  if not result:
    response = JSONResponse(content={"message":"No user found with that state"}, status_code=404)
  return response

# Create user
@user_router.post("/users/create", tags=["Users"], response_model=dict, status_code=201)
def create_user(user: User):
  db = Session()
  newUser = UserModel(**user.model_dump())
  db.add(newUser)
  db.commit()
  return JSONResponse(status_code=201, content={"message": "User created successfully."})

# Login
@user_router.post("/login", tags=["Users"], status_code=200)
def login_user(userlogin: UserLogin):
  username = userlogin.username
  password = userlogin.password
  state = "Activate"
  try:
    db = Session()
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if not user:
      return JSONResponse(content={"message": "Incorrect user"}, status_code=404)
    token = create_token(data={'user':jsonable_encoder(user)})
    res = JSONResponse(content={"token": token}, status_code=200)
    if password != user.password :
      res = JSONResponse(content={"message": "Incorrect password"}, status_code=400)
    if state != user.state:
      res = JSONResponse(content={"message": "User is inactive"}, status_code=400)
    return res
  except Exception as e:
    print("Error: ", e)
    return JSONResponse(content={"message": "Internal error"}, status_code=500)

# Update user by id
@user_router.put("/users/update/id/{userid}", tags=["Users"], status_code=200)
def update_user(userid:int, user: UserUpdate):
  db = Session()
  result = db.query(UserModel).filter(UserModel.userid == userid).first()
  if not result:
    return JSONResponse(status_code=404, content={"message": "User not found"})
  result.username = user.username
  result.phone = user.phone
  result.state = user.state
  db.commit()
  return JSONResponse(status_code=200, content={"message": "User updated successfully"})

# Update user by username
@user_router.put("/users/update/username/{username}", tags=["Users"], status_code=200)
def update_user(username: str, user: UserUpdate):
  db = Session()
  result = db.query(UserModel).filter(UserModel.username == username).first()
  if not result:
    return JSONResponse(status_code=404, content={"message": "User not found"})
  result.username = user.username
  result.phone = user.phone
  result.state = user.state
  db.commit()
  return JSONResponse(status_code=200, content={"message": "User updated successfully"})