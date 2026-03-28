from pydantic import BaseModel, ConfigDict, Field


class RegisterRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    email: str = Field(..., examples=["user@example.com"])
    password: str = Field(..., min_length=8, examples=["correcthorsebatterystaple"])


class LoginRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    email: str = Field(..., examples=["user@example.com"])
    password: str = Field(..., min_length=8, examples=["correcthorsebatterystaple"])


class TokenResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    access_token: str = Field(..., examples=["example.jwt.token"])
    token_type: str = Field(default="bearer", examples=["bearer"])