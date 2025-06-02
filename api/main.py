from fastapi import APIRouter
from api import  vendor, auth,organization  # import your route modules here

api_router = APIRouter()

# Include sub-routers under a versioned or modular path
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(vendor.router, prefix="/vendors", tags=["vendors"])
api_router.include_router(organization.router, prefix="/organizations", tags=["organizations"])