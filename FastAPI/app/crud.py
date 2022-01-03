from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from . import schema, models

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

def save_id(db: Session, connectionId: schema.ConnectionId):
    cdict = models.ConnectionId(**connectionId.dict())
    db.add(cdict)
    db.commit()
    db.refresh(cdict)
    return cdict

def get_allId(db: Session):
    print(1000000000)
    return db.query(models.ConnectionId).all()


def get_cdict(db: Session):
    return db.query(models.ConnectionDict).all()

def get_dict_column(db: Session):
    return db.query(models.ConnectionId.widget_id).all()

def get_widget_cdict(db: Session, connectionDict: schema.ConnectionDict):
    widget_id = connectionDict.widget_id
    slot = connectionDict.slot
    connectionid = connectionDict.connectionid
    return db.query(models.ConnectionDict). \
                filter(models.ConnectionDict.widget_id == widget_id). \
                filter(models.ConnectionDict.slot == slot). \
                filter(models.ConnectionDict.connectionid == connectionid).all()

def get_slot_separate(db: Session, widget_id: int, slot: str):
       return db.query(models.ConnectionDict). \
                filter(models.ConnectionDict.widget_id == widget_id). \
                filter(models.ConnectionDict.slot == slot).all()

def get_widget_cdict_separate(db: Session, widget_id: int, slot: str, connectionid: int):
    # widget_id = connectionDict.widget_id
    # slot = connectionDict.slot
    # connectionid = connectionDict.connectionid
    return db.query(models.ConnectionDict). \
                filter(models.ConnectionDict.widget_id == widget_id). \
                filter(models.ConnectionDict.slot == slot). \
                filter(models.ConnectionDict.connectionid == connectionid).all()

def delete_all_connectionDict(db: Session):
   db.query(models.ConnectionDict).delete()
   db.commit()
   return {"Details:" : "Delete All Entries Successfully"} 

def delete_slot(widget_id: int, slot: str, db: Session):
    # we are going to delete everything in the table filitering the widget and slot
    db.query(models.ConnectionDict). \
            filter(models.ConnectionDict.widget_id == widget_id). \
            filter(models.ConnectionDict.slot == slot).delete()
    db.commit()
    return {"Details" : "One slot is gone"}

def delete_connection(widget_id: int, slot: str, connectionId: int, db: Session):
    # we are going to delete everything in the table filitering three things: widget id, slot and connection id
    db.query(models.ConnectionDict). \
            filter(models.ConnectionDict.widget_id == widget_id). \
            filter(models.ConnectionDict.slot == slot). \
            filter(models.ConnectionDict.connectionid == connectionId).delete()
    db.commit()
    return {"Details" : "One Specific entry is gone"}

def is_connect_slot(widget_id: int, slot: str, db: Session):
    if get_slot_separate(db, widget_id, slot) == []:
        return False
    else:
        return True


def is_connect_connection(widget_id: int, slot: str, connectionid: int, db: Session):
    if get_widget_cdict_separate(db, widget_id, slot, connectionid) == []:
        return False
    else:
        return True

def is_set(widget_id: int, slot: str, db: Session):
    if get_cdict(db) == []:
        return False
    
    if get_slot_separate(db, widget_id, slot) == []:
       return False
    else:
        return True 

def error_message(message):
    return {
        'error': message
    }