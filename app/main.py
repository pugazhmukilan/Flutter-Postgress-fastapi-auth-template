import fastapi 
from fastapi import Depends, HTTPException , APIRouter, FastAPI
from sqlalchemy.orm import Session

import psycopg2
from psycopg2.extras import RealDictCursor
app = FastAPI()
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
def getdata():
     post = cursor.execute("""SELECT * FROM users""")
     post  = cursor.fetchall()#unless u wrtite this print post wont execute

     print(post)
     return{"result":post}

@app.post("/setdata")
def getdata():
     try:
        cursor.execute("""
            INSERT INTO users (id,username, email, password) 
            VALUES (2,'john_doe', 'john@example.com', 'securepassword123')
            
        """)
        
        conn.commit()  # Commit the transaction
        
        return {"result": "success",}
    
     except Exception as e:
          conn.rollback()  # Rollback in case of an error
          raise HTTPException(status_code=500, detail=str(e))