from app.domain.schemas.common import ErrorResponse

NOT_IMPLEMENTED_RESPONSE = {
    501: {
        "model": ErrorResponse,
        "description": "Declared in the Step 6 API shell; business logic is not implemented yet.",
    }
}