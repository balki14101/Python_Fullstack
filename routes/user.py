from unittest import result
from urllib import request
from fastapi import APIRouter,Request,Form, Response,status
from models.user import User 
from config.database import conn
from config.database import conn_user
from schemas.user import userEntity,usersEntity,serializeDict,serializeList
from bson import ObjectId
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
import json
from bson import json_util


from kafka import KafkaProducer

bootstrap_servers = ['localhost:9092']
topicName = 'myfirst'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

user = APIRouter() 
# user.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="views")


@user.get('/users')
def getAllUsers():
    return usersEntity(conn['users'].find())

@user.get('/users/{id}')
def getUser(id:str):
    user = usersEntity(conn['users'].find({'_id':ObjectId(id)}))
    if not user:
        return 'not found'
    else:            
        return user
    
@user.post('/users')
def createUser(user:User,request: Request):
    print(request)
    
    new_user = dict(user)
    # del new_user["id"]
    entered_email = new_user['email']
    check_email = conn['users'].find_one({'email':entered_email})
    #check if email exist in db
    if not check_email:
        id = conn['users'].insert_one(new_user).inserted_id
        user = conn['users'].find_one({'_id':id})
        print(new_user)
        return userEntity(user)
    else:
        return 'already existing'
    

@user.put('/users/{id}')
def updateUser(id:str,user:User):
    conn['users'].find_one_and_update({'_id':ObjectId(id)},{'$set':dict(user)})
    return user        

@user.delete('/users/{id}')
def deleteUser(id:str,response:Response):
    userEntity(conn['users'].find_one_and_delete({'_id':ObjectId(id)}))
    response.status_code=status.HTTP_204_NO_CONTENT
    return 'deleted'

###############################################################################################

#get login
@user.get("/")
async def login(request: Request):
    return templates.TemplateResponse("login.html",{'request':request})  

#post login
@user.post("/")
async def login(request: Request,email: str = Form() ,password: str = Form()):
    # email = user_email
    # password = user_password     
    data = conn['users'].find_one({'email':email})
    print(email)
    print(password)

    if(data['password']==password):
        # return {'email':email,'password':password}
        print('successful')
        # for data from socket
        streaming_data = []

        all_shipments = conn_user['mycol'].find()  

        for i in all_shipments:
            streaming_data.append(i)
        return templates.TemplateResponse("home.html",{'request':request,"streaming_data":streaming_data})
    else:
        print('invalid credentials')        
        return templates.TemplateResponse("login.html",{'request':request})        

#get signup
@user.get("/signUp")
async def signup_get(request: Request):
    
    return templates.TemplateResponse("signUp.html",{'request':request}) 

#post signup
@user.post("/signUp")
async def signup(request:Request,username:str=Form(),email:str=Form(),password:str=Form()):
    user = User(name=username,email=email,password=password)
    checkEmail = conn['users'].find_one({"email":email})
    if not checkEmail:
        conn['users'].insert_one(user.dict())
        print(user)     

        ack = producer.send(topicName, json.dumps(user.dict()).encode('utf-8'))
        # ack = producer.send('orders', json.dumps(user, default=json_util.default).encode('utf-8'))
        
        metadata = ack.get()
        print(metadata.topic)
        print(metadata.partition)
        return templates.TemplateResponse("login.html",{'request':request})
    return {"already exists"}    
    
#get logout
@user.get('/logout')
def updateUser(request:Request):
    return templates.TemplateResponse("login.html",{'request':request})

#data_streaming
@user.get("/datastream", response_class=HTMLResponse)
async def stream_page(request: Request):

    streaming_data = []

    all_shipments = conn_user['mycol'].find()  

    for i in all_shipments:
      streaming_data.append(i)

    return templates.TemplateResponse("data.html", {"request": request,"streaming_data":streaming_data})
    






