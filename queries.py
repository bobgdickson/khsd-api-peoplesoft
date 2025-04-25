from sqlalchemy.orm import Session
from orm import PurchaseOrder, PurchaseOrderDistrib

def get_po_info_from_db(session: Session, po_id: str, business_unit: str):
    po = session.query(PurchaseOrder).filter_by(po_id=po_id, business_unit=business_unit).first()
    if not po:
        return None

    distribs = (
        session.query(PurchaseOrderDistrib)
        .filter_by(po_id=po_id, business_unit=business_unit)
        .order_by(PurchaseOrderDistrib.line_nbr)
        .all()
    )

    return {
        "po_id": po.po_id,
        "business_unit": po.business_unit,
        "po_date": po.po_date.isoformat(),
        "vendor_id": po.vendor_id,
        "line_items": [
            {
                "line_number": d.line_nbr,
                "quantity": float(d.qty_po),
                "amount": float(d.merchandise_amt),
                "fund_code": d.fund_code
            }
            for d in distribs
        ]
    }
