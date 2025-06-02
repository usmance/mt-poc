from pydantic import BaseModel

class VendorCreate(BaseModel):
    name: str
    description: str
    

class VendorRead(BaseModel):
    id: int
    name: str
    description: str
    organization_id: int

    class Config:
        from_attributes = True

