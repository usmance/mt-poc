# models/user.py
from sqlalchemy import Column, Integer, String, ForeignKey
from db.session import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="vendor")  # or 'manager'
    organization_id = Column(Integer, index=True, nullable=False)


    