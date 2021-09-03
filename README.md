# FastApi + PostgreSql ReadME

I want to introduce this project in a following order: file structure, APIs and future needs.

## General Ideas about this project

- It is a FastAPI app
- PostgreSQL integration using SQLAlchemy
- Dockerfile and docker-compose integation

## How to initialize this?

```python
docker-compose up --build 
```

should start this service.

Whenever modify the code, we need to restart this image and we should be able to tell the updates.

## File Structure

— app

    — crud.py

    — database.py

    — main.py

    — models.py

    — schema.py

— docker-compose.yml

— Dockerfile

— requirement.txt

— README.md

I believe we only need to change the following four files: [curd.py](http://curd.py), main.py, models.py, and [schema.py](http://schema.py). The rest of files are for configration purposes.

[curd.py](http://curd.py) coordinates the internal services about extract out and inject data into the postgreSQL database, which is the only place we interact with the database directly.

[main.py](http://main.py) provides APIs interacting with the client.

[schema.py](http://schema.py) and [models.py](http://models.py) are a pair of class helping determine how to store the data. They usually looks very similar except for different purposes. schema.py provides a data frame for [main.py](http://main.py), and models.py provides a dataframe for PostgreSQL databases which tells how database create tables.

Here are some concret examples:

- In the curd.py, this is a common process of inject data into the database:

```python
def save_nudges_configuration(db: Session, config: schema.Configuration):
    config_model = models.Configuration(**config.dict())
    db.add(config_model)
    db.commit()
    db.refresh(config_model)
    return config_model
```

- In the main.py, we can start a simple API by the following code:

```python
@app.get("/")
def read_root():
    return {"Hello": "World 10"}
```

- In the schema.py, we could define a data frame for the service:

```python
class Configuration(BaseModel):
    modelUrl: str
    frequency: int
    federated: bool

    class Config:
        orm_mode = True
```

- In the model.py, we could define a data frame for creaing Configuration table:

```python
class Configuration(Base):
    __tablename__ = 'Configuration'
    id = Column(Integer, primary_key = True, autoincrement = True)
    modelUrl = Column(String)
    frequency = Column(Integer)
    federated = Column(Boolean)
```

## APIs

For APIs, it is easy to visit [http://localhost/docs](http://localhost/docs) for a Swagger UI, but I want to give a berif introduction here.

Generally, All the current APIs serve the purpose of replacing ConnectionDict class in BwBase.py.

We assume we will provide each widget a unique Id. Slot and ConnectionId are the esential components in order to mimic the functionalities of ConnectionDict class. 

Each Unique id, slot and connectionId will become an entry in the table.

### (POST) /connectionDict

- We could inject new entry into the ConnectionDict table.
- Forbid Repetition entry
- Autoincreate primary key for ConnectionDict table
