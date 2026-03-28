from pydantic import BaseModel, ConfigDict


class ErrorResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: str
    message: str


class MessageResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    message: str