from pydantic import BaseModel, EmailStr,ConfigDict

class UserCreate(BaseModel):
    """_summary_

    this class willl validate the user inputs structure 
    but if we give more pareneters  it will accept but it wont consider 
    those parameter for processinff and silently ignore

    but there is other way to even give error when extra parameters are given
     
    class config:
        extra = "forbid"

    this is the best practise for data integrity and security

    if u use this below the class then you can generate the error
    when extra parameter is given as ainput to the request
    """
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True


class Fetchuser(BaseModel):
    id: int
    
    class config:
        extra = "forbid"
