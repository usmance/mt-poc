# core/dependencies.py
import jwt
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import ExpiredSignatureError, InvalidTokenError


from db.session import get_db
from models.users import User
from core.config import settings
from schemas.user import UserLogin


bearer_scheme = HTTPBearer(auto_error=False)

def get_current_user(token: HTTPAuthorizationCredentials  = Depends(bearer_scheme), db: Session = Depends(get_db)) -> User:
    try:
        if not token or not token.credentials:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        payload = jwt.decode(token.credentials, settings.SECRET_KEY, algorithms=["HS256"])
        user_id: int = payload.get("id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user