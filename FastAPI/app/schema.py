from pydantic import BaseModel
from typing import Optional

# class DeviceInfo(BaseModel):
#     token: str
#     username: Optional[str]

#     class Config:
#         orm_mode = True


class Configuration(BaseModel):
    modelUrl: str
    frequency: int
    federated: bool

    class Config:
        orm_mode = True

class ConnectionDict(BaseModel):
    # id: int
    widget_id: int
    slot: str
    connectionid : int

    class Config:
        orm_mode = True