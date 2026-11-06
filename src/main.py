from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/time")
async def time():

    return {"time": datetime.datetime.now().time()}