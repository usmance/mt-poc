# models/vendor.py
from sqlalchemy import Column, Integer, String, ForeignKey
from db.session import Base

class Vendor(Base):
    __tablename__ = "vendors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    organization_id = Column(Integer, index=True, nullable=False)
