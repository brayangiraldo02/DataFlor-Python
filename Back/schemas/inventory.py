from pydantic import BaseModel, Field, constr
from enum import Enum

class InventoryState(str, Enum):
    Activate = "Activate"
    Inactive = "Inactive"

class InventoryBase(BaseModel):
    quantity: int = Field(..., gt=0)

class InventoryCreate(InventoryBase):
    idflowershops: int
    productid: int
    providerid: int
    state: InventoryState = InventoryState.Activate

class Inventory(InventoryBase):
    inventoryid: int
    idflowershops: int
    productid: int
    providerid: int
    state: InventoryState