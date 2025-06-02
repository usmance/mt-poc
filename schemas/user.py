from pydantic import BaseModel, ConfigDict, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str = "vendor"
    organization_id: int


class UserLogin(BaseModel):
    email: EmailStr
    password: str
class UserRead(BaseModel):
    id: int
    email: EmailStr
    role: str
    organization_id: int
     
    model_config = ConfigDict(from_attributes=True)
        

class LoginResponse(BaseModel):
    user: UserRead
    token: str