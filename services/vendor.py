from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from core.dependencies import get_current_user

from models.users import User
from schemas.user import UserCreate
from db.session import get_db
from services.auth import signup_user


async def get_all_vendors(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    vendors=db.query(User).filter(User.organization_id == user.organization_id, User.role=='vendor').all()
    return vendors


async def create_single_vendor(user_to_create: UserCreate, db: Session = Depends(get_db), auth_user: User = Depends(get_current_user)):
    print(user_to_create.role,auth_user.role,auth_user.organization_id,user_to_create.organization_id)
    
    if auth_user.role != 'manager' or auth_user.organization_id != user_to_create.organization_id:
        raise HTTPException(status_code=403, detail="Only managers can create vendors within their organization")
    vendor= await signup_user(user_to_create,db)
   
    return vendor