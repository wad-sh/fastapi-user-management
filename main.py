from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import *

app = FastAPI()

class Usr(BaseModel) :
    name: str
    age: int
    


@app.post("/users")
def adduser0(user: Usr) :
    if user.age < 0:
        raise HTTPException(
    status_code=400,
    detail="Invalid age"
)
    x=adduser(user.name,user.age)
    return {
        "message":"User created",
        "user":{
        "id":x,
        "name":user.name,
        "age":user.age
        }
        }


@app.get("/users")
def allusers () :
    return getallusers()

@app.get("/users/{id}")
def getuser0 (id: int) :
    user = getuser(id)  
    if user is None :
        raise HTTPException(
            status_code= 404,
            detail= "User not found"
        )
    return user

@app.delete("/users/{id}")
def deleteuser0 (id: int):
    user = getuser(id)  
    if user is None :
        raise HTTPException(
            status_code= 404,
            detail= "User not found"
        )
    deleteuser(id)
    return {
                "message":"User deleted",
                "id" : id
                }
    

@app.put("/users/{id}")
def updateuser0 (id: int, user: Usr) :
    if user.age < 0:
        raise HTTPException(
    status_code=400,
    detail="Invalid age"
)
    
    u = getuser(id)
    if u is None :
            
        raise HTTPException(
            status_code= 404,
            detail= "User not found"
        )
    
    updateuser(id,user.name,user.age)
    u = getuser(id)
    return {
                "message":"User updated",
                "user" : u
                }

class Userup (BaseModel):
    name: str | None =None
    age: int | None = None

@app.patch("/users/{id}")
def updateusernameorage (id: int, user: Userup) :
    if user.age is not None and user.age < 0:
        raise HTTPException(
    status_code=400,
    detail="Invalid age"
)
    if user.name is None and user.age is None:
        raise HTTPException(
        status_code=400,
        detail="No data provided"
    )
    u = getuser(id)
    if u is None :
            
        raise HTTPException(
            status_code= 404,
            detail= "User not found"
        )
    
    updateuser(id,user.name,user.age)
    u = getuser(id)
    return {
                "message":"User updated",
                "user" : u
                }
