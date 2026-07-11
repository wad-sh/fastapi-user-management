from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

class Usr(BaseModel) :
    name: str
    age: int
    
users =[]

@app.post("/user/")
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

