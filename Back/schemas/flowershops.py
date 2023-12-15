# Schema for FlowerShops

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

# FlowerShop Base
class FlowerShop(BaseModel):
  fullname: str = Field(..., min_length=2, max_length=255)
  address: str = Field(..., min_length=1) 
  phone: str = Field(..., min_length=1, max_length=15)

# States for FlowerShops
class FlowerShopState(str, Enum):
  Activate = "Activate"
  Inactive = "Inactive"

# FlowerShop Update
class FlowerShopUpdate(BaseModel):
  fullname: Optional[str] = Field(None, min_length=2, max_length=255)
  address: Optional[str] = Field(None, min_length=1) 
  phone: Optional[str] = Field(None, min_length=1, max_length=15)
  state: Optional[FlowerShopState] = None

# class FlowerShopCreate(FlowerShopBase):
#     state: FlowerShopState = FlowerShopState.Activate

# class FlowerShop(FlowerShopBase):
#     idflowershops: Optional[int] = None
#     state: FlowerShopState
