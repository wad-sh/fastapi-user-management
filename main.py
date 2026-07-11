from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Usr(BaseModel) :
    name: str
    age: int
    
users =[]

@app.post("/users")
def adduser(user: Usr) :
    if user.age < 0:
        raise HTTPException(
    status_code=400,
    detail="Invalid age"
)
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
def getuser (id: int) :
    for user in users :
        if user["id"] == id :
            return user
    raise HTTPException(
        status_code= 404,
        detail= "User not found"
    )

@app.delete("/users/{id}")
def deleteuser (id: int):
    for user in users :
        if user["id"] == id :
            users.remove(user)
            return {
                "message":"User deleted",
                "id" : id
                }
    raise HTTPException(
        status_code= 404,
        detail= "User not found"
    )

@app.put("/users/{id}")
def updateuser (id: int, user: Usr) :
    if user.age < 0:
        raise HTTPException(
    status_code=400,
    detail="Invalid age"
)
    
    for u in users :
        if u["id"] == id :
            u["name"] = user.name
            u["age"] = user.age
            return {
                "message":"User updated",
                "user" : u
                }
    raise HTTPException(
        status_code= 404,
        detail= "User not found"
    )

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
    for u in users :
        if u["id"] == id :
            if user.name is not None :
                u["name"] = user.name
            if user.age is not None :
                u["age"] = user.age
            return {
                "message":"User updated",
                "user" : u
                }
    raise HTTPException(
        status_code= 404,
        detail= "User not found"
    )