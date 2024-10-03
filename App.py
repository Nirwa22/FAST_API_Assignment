from fastapi import FastAPI
from typing import Union
import json
app = FastAPI()


users = [
                {"id": 1, "Name": "Sarah", "Age": 34, "Gender": "f"},
                {"id": 2, "Name": "Maha", "Age": 15, "Gender": "f"},
                {"id": 3, "Name": "Ali", "Age": 40, "Gender": "m"},
                {"id": 4, "Name": "Tahir", "Age": 63, "Gender": 'm'},
                {"id": 5, "Name": "Ayesha", "Age": 25, "Gender": "f"},
                {"id": 6, "Name": "Zahid", "Age": 23, "Gender": "m"},
             ]
@app.get("/")
def home():
    return "Home Route"
@app.get("/Users_data")
def user_data(data=users):
    new_data = json.dumps(data)
    return new_data

