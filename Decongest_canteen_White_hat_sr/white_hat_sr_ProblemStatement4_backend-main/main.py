from fastapi import FastAPI, Header, HTTPException, Depends, WebSocket , Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import jwt
import datetime
import database
import streams
import json

origins = [ '*' ]

app = FastAPI(title = "CanteenBooking")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

USER_SECRET_KEY = "usercanteenbooking"
ADMIN_SECRET_KEY = "adminusercanteenbooking"
EXPIRY_TIME = 60 * 24 * 7

class order(BaseModel):
    item_name: str
    item_qty: int

class next_orders(BaseModel):
    id:int
    user_id: str
    status: str
    items: list[order]
    order_type: int
    From : datetime.datetime
    To: datetime.datetime
    

class payload(BaseModel):
    email: str
    password: str


class booking(BaseModel):
    seat_count: int
    orders: list[order]
    start_time: datetime.datetime
    email:str


class menu_item(BaseModel):
    item_name: str
    item_price : int

class order_update(BaseModel):
    order_id_list:list[int]
    next_state:str

def get_jwt_token(email: str):
    return jwt.encode({ "email" : email ,
       'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes= EXPIRY_TIME)
    }, USER_SECRET_KEY, )

def check_jwt_token(token : str = Header(None)):
    try:
        print("inside func:"+token)
        return jwt.decode(token, USER_SECRET_KEY, algorithms=["HS256"])
    except:
        raise HTTPException(status_code=404, detail="JWT_TOKEN_NOT_FOUND")

def get_jwt_admin_token(email: str):
    return jwt.encode({ "email" : email ,
       'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes= EXPIRY_TIME)
    }, ADMIN_SECRET_KEY, )

def check_jwt_admin_token(token : str = Header(None)):
    try:
        return jwt.decode(token, ADMIN_SECRET_KEY, algorithms=["HS256"])
    except:
        raise HTTPException(status_code=404, detail="JWT_TOKEN_NOT_FOUND")




@app.post("/login",status_code = 200)
def login(pl: payload):
    if pl.password == None:
        raise HTTPException(status_code=404, detail="No Password Provided")
    else:
        auth_success = database.authenticate(pl.email,pl.password)
        if auth_success is not None: 
                new_jwt_token = get_jwt_token(pl.email)
                return {"message" : "Logged In Succesfully", "token" : new_jwt_token}
        else:
                raise HTTPException(status_code=404, detail="User name not found or invalid password")


@app.post("/register", status_code = 200)
def register( pl : payload):
    if pl.password != None:

        new_user_result = database.create_user(pl.email,pl.password)
        if(new_user_result is not None):
                new_jwt_token = get_jwt_token(pl.email)
                return { "message" : "User was registered Succesfully","token" : new_jwt_token}
                
        else:
                raise HTTPException(status_code=404, detail="User Already exists")

    else:
        raise HTTPException(status_code = 404, detail = "No password entered")




@app.post("/booking", status_code = 200)
def book_table(bk: booking):

    booking_result = database.create_contiguous_booking(bk.email,bk.seat_count,bk.start_time);
    if(booking_result is not None):
        #create the order
        order_list = []
        for i in bk.orders:
            order_list.append({"item_qty":i.item_qty,"item_name":i.item_name})

        order_creation_result = database.create_order(bk.email,order_list,bk.start_time)

        if(order_creation_result is not None):

            res_dict = {"status":"success"}
            res_dict.update(order_creation_result)
            res_dict.update(booking_result)
            res_dict["email"] = bk.email
            res_dict["seat_count"] = bk.seat_count
            res_dict["start_time"] = bk.start_time
            res_dict["orders"] = order_list
            return res_dict
        else:
            res = {"status":"failure","error":"order creation failed"}
            return res
    else:
        res = {"status":"failure","error":"Bookings full"}
        return res



#ORDER Endpoints
@app.get("/orders",status_code = 200,response_model = list[next_orders])
def get_orders():
    """ Returns the orders from current_time to current_time +3 to the frontend. Let the fronend categorise the order into (today, tomorrow, so and so forth)"""
    order_list = database.get_orders()
    if order_list is not None:
        return order_list
    else:
        return HTTPException(status_code=404, detail = "error,cannot find error ID")

@app.put("/orders", status_code = 200)
def update_order(ou: order_update):
    """ updates the order """
    order_list = []

    order_update_result = database.update_order(ou.order_id_list,ou.next_state)
    if(order_update_result is not None):

        return order_update_result
    else:

        raise HTTPException(status_code = 404, detail= "order updation failed")

#LISTENERS 
@app.websocket("/ws/notifications/orderstatus/{order_id}")
async def order_status(websocket: WebSocket, order_id: str):

    await websocket.accept()
    while True:
        client_data = await websocket.receive_text()
        modified_order_document = streams.get_order_update(order_id)
        modified_order_document_string = json.dumps(modified_order_document)
        await websocket.send_text(modified_order_document)


@app.websocket("/ws/notifications/neworders")
async def new_order(websocket: WebSocket):

    await websocket.accept()
    time_quantum = None
    while True:
        client_data = await websocket.receive_text()
        client_data = json.loads(client_data)
        if time_quantum is not None:
            new_ord = streams.get_new_order(time_quantum)
            new_ord_string = json.dumps(new_ord)
            await websocket.send_text(new_ord_string)

        elif("time_quantum" in client_data):
            time_quantum = client_data["time_quantum"]
            await websocket.send_text(json.dumps({"message":"time_quantum_recieved"}))

        


#ADMIN ENDPOINTS
@app.post("/admin/login",status_code = 200)
def admin_login(pl: payload):
    if pl.password == None:
        raise HTTPException(status_code=404, detail="No Password Provided")
    else:
        auth_success = database.authenticate_admin(pl.email,pl.password)
        if auth_success is not None: 
                new_jwt_token = get_jwt_admin_token(pl.email)
                return {"message" : "Logged In Succesfully", "token" : new_jwt_token}
        else:
                raise HTTPException(status_code=404, detail="User Not Found")


@app.post("/admin/register", status_code = 200)
def admin_register(pl : payload):
    if pl.password != None:

        new_user_result = database.create_admin(pl.email,pl.password)
        if(new_user_result is not None):
                new_jwt_token = get_jwt_admin_token(pl.email)
                return { "message" : "User was registered Succesfully","token" : new_jwt_token}
                
        else:
                raise HTTPException(status_code=404, detail="User Already exists")

    else:
        raise HTTPException(status_code = 404, detail = "No password entered")






