class ServiceNotImplementedError(Exception):
    def __init__(self, operation: str) -> None:
        self.operation = operation
        super().__init__(
            f"{operation} is part of the Step 6 API shell and will be implemented in a later step."
        )