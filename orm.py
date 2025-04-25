from sqlalchemy import Column, String, Integer, DateTime, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from database import Base

class PurchaseOrder(Base):
    __tablename__ = "PS_PO_HDR"
    business_unit = Column(String, primary_key=True, name="BUSINESS_UNIT")
    po_id = Column(String, primary_key=True, name="PO_ID")
    po_date = Column(DateTime, name="PO_DT")
    vendor_id = Column(String, name="VENDOR_ID")

class PurchaseOrderLine(Base):
    __tablename__ = "PS_PO_LINE"
    business_unit = Column(String, primary_key=True, name="BUSINESS_UNIT")
    po_id = Column(String, primary_key=True, name="PO_ID")
    line_nbr = Column(Integer, primary_key=True, name="LINE_NBR")

class PurchaseOrderDistrib(Base):
    __tablename__ = "PS_PO_LINE_DISTRIB"
    business_unit = Column(String, primary_key=True, name="BUSINESS_UNIT")
    po_id = Column(String, primary_key=True, name="PO_ID")
    line_nbr = Column(Integer, primary_key=True, name="LINE_NBR")
    distrib_line_num = Column(Integer, primary_key=True, name="DISTRIB_LINE_NUM")
    qty_po = Column(DECIMAL, name="QTY_PO")
    merchandise_amt = Column(DECIMAL, name="MERCHANDISE_AMT")
    fund_code = Column(String, name="FUND_CODE")
