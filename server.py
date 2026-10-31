from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

app = FastAPI(title="ELEN Auth Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # باز کردن CORS برای تست قطعی
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AuthRequest(BaseModel):
    email: str
    password: str
    username: str | None = None

@app.get("/")
@app.get("/api/health")
def health():
    return {"status": "ok", "ts": int(time.time())}

@app.post("/api/auth/register")
def register(req: AuthRequest):
    return {"status": "ok", "message": "User registered (mock)", "user": {"email": req.email}}

@app.post("/api/auth/login")
def login(req: AuthRequest):
    return {"status": "ok", "token": "mock_jwt_token_" + req.email, "user": {"email": req.email}}
