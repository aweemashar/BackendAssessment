from os import environ

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": f"App is running on port. {environ.get('SOCIAL_PORT')}"}
