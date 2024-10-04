from fastapi import FastAPI, Request
from dotenv import load_dotenv
from pydantic import BaseModel
import json
import os
import uuid


load_dotenv()
api_key = os.getenv("SECRET_API_KEY")

app = FastAPI()

with open("user.json", "r") as json_file:
    Users_data = json.load(json_file)


class Item(BaseModel):
    Name: str | None = None
    Age: int | None = None
    Gender: str | None = None
    id: str | None = None


@app.get("/")
async def home():
    return {"Home Route"}


@app.get("/Users_data")
async def user_data():
    return Users_data


@app.post("/add")
def add(item: Item):
    return item


@app.post("/Add_Users_data")
async def add_data(item: Item, request: Request):
    api = request.headers.get("Authorization")
    user_info = {"Name": item.Name, "Age": item.Age, "Gender": item.Gender}
    if api and api != api_key:
        return "Unauthorized access"
    elif not api:
        return "API_Key needed"
    elif api == api_key:
        session_id = uuid.uuid4()
        user_info["id"] = str(session_id)
        with open("user.json", "a") as newuser_file:
            json.dump(user_info, newuser_file, indent=4)
        return f"Authorization Successful: Your session_id is {session_id}"

@app.post("/Get_User_Information")
async def get_data(item: Item, request: Request):
    api = request.headers.get("Authorization")
    if api and api != api_key:
        return "Unauthorized Access"
    elif not api:
        return "Api Key needed"
    elif api == api_key:
        with open("user.json", "r") as file:
            users_information = json.load(file)
        for i in users_information:
            if i["id"] == item[4]:
                return {"Name": i["Name"], "Age": i["Age"], "Gender": i["Gender"]}
                break
        return {"Error Occured: Session_id does not exist"}




