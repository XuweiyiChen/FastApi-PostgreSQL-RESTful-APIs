from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from . import schema, models


# def save_device_info(db: Session, info: schema.DeviceInfo):
#     device_info_model = models.DeviceInfo(**info.dict())
#     db.add(device_info_model)
#     db.commit()
#     db.refresh(device_info_model)
#     return device_info_model

# def get_device_info(db: Session, token: str = None):
#     if token is None:
#         return db.query(models.DeviceInfo).all()
#     else:
#         return db.query(models.DeviceInfo).filter(models.DeviceInfo.token == token).first()

def save_nudges_configuration(db: Session, config: schema.Configuration):
    config_model = models.Configuration(**config.dict())
    db.add(config_model)
    db.commit()
    db.refresh(config_model)
    return config_model

def get_nudges_configuration(db: Session):
    return db.query(models.Configuration).first()

def delete_nudges_configuration(db: Session):
    db.query(models.Configuration).delete()

def save_cdict(db: Session, connectionDict: schema.ConnectionDict):
    cdict = models.ConnectionDict(**connectionDict.dict())
    db.add(cdict)
    db.commit()
    db.refresh(cdict)
    return cdict

def get_cdict(db: Session):
    return db.query(models.ConnectionDict).all()

def get_widget_cdict(db: Session, connectionDict: schema.ConnectionDict):
    widget_id = connectionDict.widget_id
    slot = connectionDict.slot
    connectionid = connectionDict.connectionid
    return db.query(models.ConnectionDict). \
                filter(models.ConnectionDict.widget_id == widget_id). \
                filter(models.ConnectionDict.slot == slot). \
                filter(models.ConnectionDict.connectionid == connectionid).all()

def delete_all_connectionDict(db: Session):
   db.query(models.ConnectionDict).delete()
   db.commit()
   return {"Details:" : "Delete All Entries Successfully"} 

def error_message(message):
    return {
        'error': message
    }