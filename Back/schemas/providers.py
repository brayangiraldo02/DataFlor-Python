# Schema for Providers

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

# Providers Base
class Providers(BaseModel):
    fullname: str = Field(..., min_length=2, max_length=255)
    address: str = Field(..., min_length=1) 
    phone: str = Field(..., min_length=1, max_length=15)

# States for providers
class ProvidersState(str, Enum):
    Activate = "Activate"
    Inactive = "Inactive"

# Providers Update
class ProvidersUpdate(BaseModel):
    fullname: Optional[str] = Field(None, min_length=2, max_length=255)
    address: Optional[str] = Field(None, min_length=1) 
    phone: Optional[str] = Field(None, min_length=1, max_length=15)
    state: Optional[ProvidersState] = None
