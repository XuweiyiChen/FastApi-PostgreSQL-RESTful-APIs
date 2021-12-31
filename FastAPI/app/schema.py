from pydantic import BaseModel
from typing import Optional

class ConnectionDict(BaseModel):
    widget_id: int
    slot: str
    connectionid: int

    class Config:
        orm_mode = True

class ConnectionId(BaseModel):
    widget_id: int
    widget_name: str

    class Config:
        orm_mode = True