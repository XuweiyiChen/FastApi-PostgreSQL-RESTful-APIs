from pydantic import BaseModel
from typing import Optional

class Configuration(BaseModel):
    modelidentity: str
    frequency: int
    federated: bool

    class Config:
        orm_mode = True

class ConnectionDict(BaseModel):
    widget_id: int
    slot: str
    connectionid: int

    class Config:
        orm_mode = True

class ConnectionId(BaseModel):
    widgetid: int
    widgetname: str

    class Config:
        orm_mode = True