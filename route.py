from fastapi import FastAPI, Depends, HTTPException, Body
from docker_con1.controllers.generate_pass3 import passwordInto_hash3, passswordIntoHash3
from docker_con1.model import create_db_and_tables
from sqlmodel import Session, select
from typing import Annotated
from typing import AsyncGenerator
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI)-> AsyncGenerator[None, None]:
    print("Creating tables..")
    create_db_and_tables()
    yield

app = FastAPI()

@app.get('/')
def get_root():
    return {"Docker ": "Compose Image"}

# Define a route to generate a password hash
@app.get("/api/get_password3")
def generate_pass3():
    passwordInto_hash3()  # admin hash-password on terminal
    return passswordIntoHash3("user_password123")  # user hash-password on swagger (response body)
