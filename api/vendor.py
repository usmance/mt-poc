from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from models.users import User
from db.session import get_db
from core.dependencies import get_current_user
from services.vendor import get_all_vendors, create_single_vendor
from schemas.user import UserRead, UserCreate


router = APIRouter()

@router.get("/", response_model=list[UserRead])
async def get_vendors(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    vendors= await get_all_vendors(db,user)
    return vendors


#Assuming that only an organization manager can create a vendor.
@router.post("/", response_model=UserCreate)
async def create_vendor(user_to_create: UserCreate, db: Session = Depends(get_db), auth_user: User = Depends(get_current_user)):
    vendor_creation= await create_single_vendor(user_to_create,db,auth_user)
    return vendor_creation