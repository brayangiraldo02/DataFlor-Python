from pydantic import BaseModel, Field, constr
from enum import Enum

class ProductState(str, Enum):
    Available = "Available"
    Unavailable = "Unavailable"

class ProductBase(BaseModel):
    productname: constr(min_length=2, max_length=255)
    description: str = None  # Puedes ajustar el manejo de valores nulos según tus necesidades
    price: float = Field(..., gt=0)

class ProductCreate(ProductBase):
    state: ProductState = ProductState.Available

class Product(ProductBase):
    productid: int
    state: ProductState
