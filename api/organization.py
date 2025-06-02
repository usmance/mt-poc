from typing import List, Optional
from fastapi import APIRouter, HTTPException, status, Depends
from db.session import SessionLocal
from sqlalchemy.orm import Session
from models.organizations import Organization
from schemas.organization import OrganizationCreate, OrganizationRead
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrganizationRead, status_code=status.HTTP_201_CREATED)
async def create_organization(org: OrganizationCreate, db: Session = Depends(get_db)):
    db_org = Organization(name=org.name)
    db.add(db_org)
    db.commit()
    db.refresh(db_org)
    return db_org
