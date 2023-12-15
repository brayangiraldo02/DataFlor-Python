'''
  Developed by Brayan Cataño Giraldo.
  E-mail: b.catano@utp.edu.co
'''

'''
  This file contains the User schema.
  It is used to validate the User data.
'''
# Importing libraries
from pydantic import BaseModel, Field, constr
from typing import Optional
from enum import Enum

# User Role
class UserRole(str, Enum):
  Admin = "Admin"
  Dueño = "Dueño"
  Empleado = "Empleado"

# User State
class UserState(str, Enum):
  Activate = "Activate"
  Inactive = "Inactive"

# User Base
class User(BaseModel):
  username: constr(min_length=1, max_length=50)
  password: constr(min_length=1, max_length=255)
  fullname: constr(min_length=1, max_length=255)
  phone: constr(min_length=1, max_length=15)
  role: UserRole
  idflowershops: int = None

# User Update
class UserUpdate(BaseModel):
  username: constr(min_length=1, max_length=50)
  phone: constr(min_length=1, max_length=15)
  state: Optional[UserState] = None

# User Login
class UserLogin(BaseModel):
  username: constr(min_length=1, max_length=50)
  password: constr(min_length=1, max_length=255)
  # state: Optional[UserState] = None