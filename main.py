from fastapi import *
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

class Usr(BaseModel) :
    name: str
    age: int
    
users =[]

@app.post("/users")
def adduser(user: Usr) :
    if user.age < 0:
        return {
            "message": "Error: Invalid age.",
            "user": None
        }
    x = Gid()
    users.append({
        "id":x,
        "name":user.name,
        "age":user.age
        })
    return {
        "message":"User created",
        "user":{
        "id":x,
        "name":user.name,
        "age":user.age
        }
        }

def Gid() :
    max = 0
    for user in users :
        if user["id"] > max :
            max = user["id"]
    return max+1

@app.get("/users")
def allusers () :
    return users

@app.get("/users/{id}")
def getuser (uid: int) :
    for user in users :
        if user["id"] == uid :
            return user
    raise HTTPException(
        status_code= 404
        detail= "User not found"
    )

