import dataclasses

import fastapi
from result import Err, Ok

from ....app.dependencies import Service

auth = fastapi.APIRouter(prefix="/auth", tags=["auth"])


@dataclasses.dataclass
class AuthenticationResponse:
    first_name: str
    last_name: str
    email: str
    password: str


@dataclasses.dataclass
class RegisterRequest:
    first_name: str
    last_name: str
    email: str
    password: str


@auth.post("/register", response_model=AuthenticationResponse, name="auth:register")
def example(_: RegisterRequest, reg_service: Service) -> AuthenticationResponse:
    return AuthenticationResponse(**reg_service.get_value())
