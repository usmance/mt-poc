# --- routers/auth.py ---
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

from db.session import get_db
from models.users import User
from core.security import hash_password,verify_password,create_jwt_token
from schemas.user import UserCreate, UserLogin, UserRead

async def signup_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = User(
        email=user.email,
        hashed_password=hash_password(user.password),
        role=user.role,
        organization_id=user.organization_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    user_dict = UserRead.model_validate(db_user).model_dump()
    return {
        "user":user_dict,
        "token": create_jwt_token({**user_dict})
    }  
    
