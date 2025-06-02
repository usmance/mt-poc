import jwt
from core.config import settings
from passlib.context import CryptContext
from datetime import datetime, timedelta



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")




def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_jwt_token(data: dict, algorithm: str = "HS256") -> str:
    """
    Create a JWT token with the given data and expiration time.
    """
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(seconds=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60)
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=algorithm)
def decode_jwt_token(token: str, algorithms: list = ["HS256"]) -> dict:
    """
    Decode a JWT token and return the payload.
    """
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=algorithms)
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")


