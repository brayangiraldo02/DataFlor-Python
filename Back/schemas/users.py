from pydantic import BaseModel, Field, constr
from typing import Optional
from enum import Enum

class UserRole(str, Enum):
  Admin = "Admin"
  Dueño = "Dueño"
  Empleado = "Empleado"

class UserState(str, Enum):
  Activate = "Activate"
  Inactive = "Inactive"

class User(BaseModel):
  username: constr(min_length=1, max_length=50)
  password: constr(min_length=1, max_length=255)
  fullname: constr(min_length=1, max_length=255)
  phone: constr(min_length=1, max_length=15)
  role: UserRole
  idflowershops: int = None

class UserUpdate(BaseModel):
  username: constr(min_length=1, max_length=50)
  phone: constr(min_length=1, max_length=15)
  state: Optional[UserState] = None

class UserLogin(BaseModel):
  username: constr(min_length=1, max_length=50)
  password: constr(min_length=1, max_length=255)
  # state: Optional[UserState] = None