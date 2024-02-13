import fastapi

from .authetication_controller import auth

Authcontroller = fastapi.APIRouter()
Authcontroller.include_router(auth, tags=["auth"])
