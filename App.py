from fastapi import FastAPI
from typing import Union
from fastapi.params import Body
from dotenv import load_dotenv
import json
import os

load_dotenv()
api_key = os.getenv("SECRET_API_KEY")
app = FastAPI()

with open("user.json", "r") as json_file:
    Users_data = json.load(json_file)


@app.get("/")
def home():
    return {"Home Route"}


@app.get("/Users_data")
def user_data():
    return Users_data


@app.post("/post")
def post():
    return {"Message": "Post Created"}
@app.post("/Add_Users_data")
def add_data(turtle: dict = Body(...)):
    return {turtle["id"]}



