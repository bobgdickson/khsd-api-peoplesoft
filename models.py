from pydantic import BaseModel
from typing import List

class POLineItem(BaseModel):
    line_number: int
    quantity: int
    amount: float
    fund_code: str

class POResponse(BaseModel):
    po_id: str
    business_unit: str
    po_date: str
    vendor_id: str
    line_items: List[POLineItem]
