from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from models import POResponse
from database import SessionLocal
from queries import get_po_info_from_db

app = FastAPI(title="KHSD PeopleSoft Info API", version="1.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/po-info", response_model=POResponse)
def fetch_po_info(
    po_id: str = Query(...),
    business_unit: str = Query("KERNH"),
    db: Session = Depends(get_db)
):
    result = get_po_info_from_db(db, po_id, business_unit)
    if not result:
        raise HTTPException(status_code=404, detail="PO not found")
    return result
