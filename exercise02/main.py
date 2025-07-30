from fastapi import FastAPI, Query, Request, HTTPException, Body  
from pydantic import BaseModel

app = FastAPI()

class Secret(BaseModel):
    secret_code: int

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
async def top_secret(request: Request, secret: Secret = Body(...)):
    auth = request.headers.get("Authorization")
    if auth != "my-secret-key":
        raise HTTPException(status_code=403, detail="Invalid authorization key")

    code_str = str(secret.secret_code)
    if len(code_str) != 4 or not code_str.isdigit():
        raise HTTPException(status_code=400, detail="Secret code must be a 4-digit number")
    
    return {"code": secret.secret_code}