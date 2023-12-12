from pydantic import BaseModel, Field, constr
from enum import Enum

class ProviderState(str, Enum):
    Activate = "Activate"
    Inactive = "Inactive"

class ProviderBase(BaseModel):
    fullname: constr(min_length=2, max_length=255)
    phone: constr(min_length=1, max_length=15)
    address: str = None

class ProviderCreate(ProviderBase):
    state: ProviderState = ProviderState.Activate

class Provider(ProviderBase):
    providerid: int
    state: ProviderState
