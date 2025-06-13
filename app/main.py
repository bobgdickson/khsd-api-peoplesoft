from fastapi import FastAPI, Depends, HTTPException, Query, Header
from sqlalchemy.orm import Session
from app.models import POResponse
from app.database import SessionLocal, API_KEY
from app.queries import get_po_info_from_db

API_KEY_NAME = "X-API-Key"

app = FastAPI(title="KHSD PeopleSoft Info API", version="1.0")

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/po-info", response_model=POResponse, dependencies=[Depends(verify_api_key)])
def fetch_po_info(
    po_id: str = Query(...),
    business_unit: str = Query("KERNH"),
    db: Session = Depends(get_db)
):
    result = get_po_info_from_db(db, po_id, business_unit)
    if not result:
        raise HTTPException(status_code=404, detail="PO not found")
    return result
