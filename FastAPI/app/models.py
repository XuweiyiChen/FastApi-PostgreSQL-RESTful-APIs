from .database import Base
from sqlalchemy import Column, String, Boolean, Integer

class ConnectionDict(Base):
    __tablename__ = 'Connectiondict'
    id = Column(Integer, primary_key = True)
    widget_id = Column(Integer)
    slot = Column(String)
    connectionid = Column(Integer)

class ConnectionId(Base):
    __tablename__ = 'Connectionid'
    # id = Column(Integer, primary_key = True)
    widget_id = Column(Integer, primary_key = True)
    widget_name = Column(String)

class Configuration(Base):
    __tablename__ = 'Configuration'
    id = Column(Integer, primary_key = True, autoincrement = True)
    modelUrl = Column(String)
    frequency = Column(Integer)
    federated = Column(Boolean)