from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class FlowerShopState(str, Enum):
    Activate = "Activate"
    Inactive = "Inactive"

class FlowerShopBase(BaseModel):
    fullname: str = Field(..., min_length=2, max_length=255)
    address: str = Field(..., min_length=1) 
    phone: str = Field(..., min_length=1, max_length=15)

class FlowerShopCreate(FlowerShopBase):
    state: FlowerShopState = FlowerShopState.Activate

class FlowerShop(FlowerShopBase):
    idflowershops: Optional[int] = None
    state: FlowerShopState
