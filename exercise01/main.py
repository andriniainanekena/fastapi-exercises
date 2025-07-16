from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

@app.get("/hello")
def read_hello(name: str = Query(default="Nekena")):
    return f"Hello {name} !"

class WelcomeRequest(BaseModel):
    name: str = "Nekena"

@app.post("/welcome")
def welcome_user(request: WelcomeRequest):
    return {"message": f"Bienvenue {request.name}"}
