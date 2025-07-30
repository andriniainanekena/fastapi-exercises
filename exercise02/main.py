from fastapi import FastAPI, Query, Request, HTTPException
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
    
@app.put("/top-secret")
async def top_secret(request: Request):
    auth = request.headers.get("Authorization")
    if auth != "my-secret-key":
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"message": "Top secret data accessed successfully!"}

