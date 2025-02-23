import fastapi 
from fastapi import Depends, HTTPException , APIRouter, FastAPI,status
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
from . import schemas
from . import utils
from pydantic import BaseModel, EmailStr


models.Base.metadata.create_all(bind = engine) 

app = FastAPI()

def get_db():
     """Eveery time when we get any request from the API we will
      get the database session for that request and  do some operation in the database
       and then close it after the operation gets closed
       """
     db = SessionLocal()
     try:
          yield db
     finally:
          db.close()


try:
     conn = psycopg2.connect(host = "localhost",database = 'fastapi',user = "postgres",password = "Pugazh2004",cursor_factory=RealDictCursor)
     cursor = conn.cursor()
     print("database connected")
except:
     print("database not connected")



@app.get("/")
def home():
    return {"result":"hello world"}



@app.get("/data")
def getdata(db: Session = Depends(get_db)):
     post = db.query(models.User).all()
     return{"result":post}




@app.post("/createuser",status_code= status.HTTP_201_CREATED,response_model = schemas.UserOut)
def usercreate(user: schemas.UserCreate,db:Session = Depends(get_db)):
     hashed_password = utils.hashpassword(user.password)
     user.password = hashed_password
     newuser = models.User(username= user.username, email=user.email, password = user.password)
     db.add(newuser)
     db.commit()
     db.refresh(newuser)
    
     return newuser
     


# @app.get("/fetch")
# def get_user(fetch: schemas.Fetchuser , db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == fetch.id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return {"result": user}
"""Use can use any of these methodds """
@app.get("/fetch",response_model = schemas.UserOut)
def get_user(id: int , db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    print(user)
    return user


