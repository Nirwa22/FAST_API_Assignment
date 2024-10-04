from fastapi import FastAPI
from fastapi.params import Body
from dotenv import load_dotenv
from pydantic import BaseModel
import json
import os


load_dotenv()
api_key = os.getenv("SECRET_API_KEY")

app = FastAPI()

with open("user.json", "r") as json_file:
    Users_data = json.load(json_file)


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
async def home():
    return {"Welcome"}


@app.get("/Users_data")
async def user_data():
    return Users_data


@app.post("/Add_Users_data")
async def add_data(item: Item):
    return item

