from fastapi import FastAPI, Depends, HTTPException
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from .schema import ConnectionDict, Configuration
from . import crud, models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World 10"}

# @app.post('/device/info')
# def save_device_info(info: DeviceInfo, db=Depends(db)):
#     object_in_db = crud.get_device_info(db, info.token)
#     if object_in_db:
#         raise HTTPException(400, detail= crud.error_message('This device info already exists'))
#     return crud.save_device_info(db,info)

# @app.get('/device/info/{token}')
# def get_device_info(token: str, db=Depends(db)):
#     info = crud.get_device_info(db,token)
#     if info:
#         return info
#     else:
#         raise HTTPException(404, crud.error_message('No device found for token {}'.format(token)))

# @app.get('/device/info')
# def get_all_device_info(db=Depends(db)):
#     return crud.get_device_info(db)

@app.post('/configuration')
def save_configuration(config: Configuration, db=Depends(db)):
    # always maintain one config
    # crud.delete_nudges_configuration(db)
    return crud.save_nudges_configuration(db, config)

@app.get('/configuration')
def get_configuration(db=Depends(db)):
    config = crud.get_nudges_configuration(db)
    if config:
        return config
    else:
        raise HTTPException(404, crud.error_message('No configuration set'))

@app.get('/connectionDict')
def get_connectionDict(db=Depends(db)):
    connectionId = crud.get_cdict(db)
    if connectionId:
        return connectionId
    else:
       raise HTTPException(404, crud.error_message('No connectionId found'))

@app.post('/connectionDict/search')
def get_connectionDict_search(connectionDict: ConnectionDict, db=Depends(db)):
    connectionId = crud.get_cdict(db, connectionDict)
    if connectionId:
        return connectionId
    else:
       raise HTTPException(404, crud.error_message('No connectionId found'))     

@app.get('/connectionDict/delete')
def delete_all_connectionDict(db=Depends(db)):
    # only for development
    delete_info = crud.delete_all_connectionDict(db)
    if delete_info:
        return delete_info
    else:
       raise HTTPException(404, crud.error_message('Cannot Process Delete. Please Retry')) 

@app.post('/connectionDict')
def save_connectionDict(connectionDict: ConnectionDict, db=Depends(db)):
    # just for safety purpose, fastapi handles the following exceptions using
    # code 422: error: Unprocessable entity

    # might revise it for future
    if connectionDict.widget_id is None:
        return HTTPException(status_code=403, detail="No widget id has been provided")
    if connectionDict.slot is None:
       return HTTPException(status_code=403, detail="No slot id has been provided")
    if connectionDict.connectionid is None:
       return HTTPException(status_code=403, detail="No connection id has been provided")
    if not type(connectionDict.widget_id) is int:
        return HTTPException(status_code=403, detail="Widget ID type should be Integer")
    if not type(connectionDict.slot) is str:
        return HTTPException(status_code=403, detail="Slot ID type should be String")    
    if not type(connectionDict.connectionid) is int:
        return HTTPException(status_code=403, detail="Connection Id type should be integer")
    
    # stop reptition entry in the tabele
    reptition = crud.get_widget_cdict(db, connectionDict)
    if reptition:
       return HTTPException(status_code=402, 
                            detail="Already had this entry.",
                            headers={"Input-Error": "We have seen same entry before."},
       ) 

    return crud.save_cdict(db, connectionDict)