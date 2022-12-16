from uuid import UUID
from pydantic import BaseModel

# Token Authentication Schema
class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


# Token Authentication Payload
class TokenPayload(BaseModel):
    sub: UUID = None
    exp: int = None
