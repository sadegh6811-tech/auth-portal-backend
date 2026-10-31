from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Elen Auth Portal Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Auth Portal Backend is running"}

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/api/auth/login")
def login(req: LoginRequest):
    return {"access_token": "mock_token_12345", "token_type": "bearer", "user": req.username}

@app.post("/api/karami/trade")
def karami_trade(authorization: str = Header(None)):
    return {"success": True, "log": ">> KARAMI ENGINE v2.0 INITIALIZED...\n>> QUANTUM TRADING MODULE ACTIVE...\n>> SUCCESS. 3 TRADES COMPLETED."}

@app.get("/api/market")
def market_data():
    return {"success": True, "data": [{"symbol": "BTCUSDT", "price": 65000.5}, {"symbol": "ETHUSDT", "price": 3500.2}]}

@app.post("/api/mathbot/discover")
def mathbot_discover():
    return {"success": True, "log": ">> MATHBOT DISCOVERY STARTED...\n>> FOUND NEW EQUATION: E = mc^2"}
