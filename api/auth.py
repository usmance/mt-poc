# --- routers/auth.py ---
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from db.session import get_db
from models.users import User
from services.auth import  signup_user,login_user
from core.dependencies import get_current_user
from schemas.user import LoginResponse, UserCreate, UserLogin, UserRead

router = APIRouter()

@router.post("/signup", response_model=UserRead)
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    return await signup_user(user,db)

@router.post("/login", response_model=LoginResponse)
async def login(user: UserLogin, db: Session = Depends(get_db)):
    return await login_user(user, db)

@router.get("/me", response_model=UserRead)
async def get_me(user: User = Depends(get_current_user)):
    return UserRead.model_validate(user)