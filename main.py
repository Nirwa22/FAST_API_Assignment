from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
import json
import os
import uuid


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization"]
)


class Item(BaseModel):
    Name: str | None = None
    Age: int | None = None
    Gender: str | None = None
    id: str | int | None = None


load_dotenv()
api_key = os.getenv("SECRET_API_KEY")


with open("user.json", "r") as json_file:
    Users_data = json.load(json_file)


@app.get("/")
async def home():
    return {"Home Route"}


@app.get("/Users_data")
async def user_data():
    return Users_data


@app.post("/Add_Users_data")
async def add_data(item: Item, request: Request):
    api = request.headers.get("Authorization")
    if api and api != api_key:
        return "Unauthorized access"
    elif not api:
        return "API_Key needed"
    elif api == api_key :
        try:
            session_id = str(uuid.uuid4())
            user_info = {"id": session_id, "Name": item.Name, "Age": item.Age, "Gender": item.Gender}
            Users_data.append(user_info)
            with open("user.json", "w") as new_user_file:
                json.dump(Users_data, new_user_file, indent=4)
            return f"Authorization Successful: Your session_id is {session_id}"
        except Exception:
            return "Message: Error Occured"
@app.post("/Get_User_Information")
async def get_data(item: Item, request: Request):
    api = request.headers.get("Authorization")
    if api and api != api_key:
        return "Unauthorized Access"
    elif not api:
        return "Api Key needed"
    elif api == api_key:
        try:
            with open("user.json", "r") as file:
                users_information = json.load(file)
            for i in users_information:
                if i["id"] == item.id:
                    return {"Name": i["Name"], "Age": i["Age"], "Gender": i["Gender"]}
                    break
                return {"Error Occured: Session_id does not exist"}
        except Exception:
            return "Message: Error Occured"





