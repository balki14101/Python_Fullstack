from unittest import result
from fastapi import APIRouter,Request,Form, Response,status
from models.user import User 
from config.database import conn
from schemas.user import userEntity,usersEntity,serializeDict,serializeList
from bson import ObjectId
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



user = APIRouter() 
user.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@user.get('/users')
def getAllUsers():
    return usersEntity(conn.local.user.find())

@user.get('/users/{id}')
def getUser(id:str):
    user = usersEntity(conn.local.user.find({'_id':ObjectId(id)}))
    if not user:
        return 'not found'
    else:            
        return user
    
@user.post('/users')
def createUser(user:User):
    new_user = dict(user)
    # del new_user["id"]
    entered_email = new_user['email']
    check_email = conn.local.user.find_one({'email':entered_email})
    #check if email exist in db
    if not check_email:
        id = conn.local.user.insert_one(new_user).inserted_id
        user = conn.local.user.find_one({'_id':id})
        print(new_user)
        return userEntity(user)
    else:
        return 'already existing'
    

@user.put('/users/{id}')
def updateUser(id:str,user:User):
    conn.local.user.find_one_and_update({'_id':ObjectId(id)},{'$set':dict(user)})
    return user        

@user.delete('/users/{id}')
def deleteUser(id:str,response:Response):
    userEntity(conn.local.user.find_one_and_delete({'_id':ObjectId(id)}))
    response.status_code=status.HTTP_204_NO_CONTENT
    return 'deleted'







