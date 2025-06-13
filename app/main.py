from fastapi import FastAPI, Depends, HTTPException, Query, Header, status
from sqlalchemy.orm import Session
from app.models import POResponse
from app.database import SessionLocal, API_KEY
from app.queries import get_po_info_from_db
from typing import Union, Optional

API_KEY_NAME = "X-API-Key"

app = FastAPI(title="KHSD PeopleSoft Info API", version="1.0")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://localhost:3000"] etc.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def verify_bearer_token(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid Authorization header")
    
    token = authorization.replace("Bearer ", "")
    if token != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/po-info", response_model=POResponse, dependencies=[Depends(verify_bearer_token)])
def fetch_po_info(
    po_id: Union[str, int] = Query(..., description="PO ID to look up", example="216154"),
    business_unit: str = Query("KERNH", description="Business Unit", example="KERNH"),
    db: Session = Depends(get_db)
):
    result = get_po_info_from_db(db, po_id, business_unit)
    if not result:
        raise HTTPException(status_code=404, detail="PO not found")
    return result
