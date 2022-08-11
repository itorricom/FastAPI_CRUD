from typing import Optional
from pydantic import BaseModel

class UserRequestModel(BaseModel):
    username : str
    email: Optional[str] = None

class UserResponseModel(UserRequestModel):
    id: int
