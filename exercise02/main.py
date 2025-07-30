from fastapi import FastAPI, Query, Request
from pydantic import BaseModel

app = FastAPI()

@app.get("/hello")
def read_hello(name: str = Query(default=None), is_teacher: bool = Query(default=None), request: Request = None):
    if name is None and is_teacher is None:    
        return "Hello World!"
    if name is None:
        name = "Undefined"
    if is_teacher is None:
        is_teacher = False
    if is_teacher:
        return f"Hello Teacher {name}!"
    else:
        return f"Hello {name}!"