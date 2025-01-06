class ServiceResponse:
    """Special class designed for inter-app communication. Supports if true check."""

    def __init__(self, status: bool, data=None, error=None, reason=None, message=None):
        self.status = status
        self.data = data
        self.error = error
        self.reason = reason
        self.message = message

    def __repr__(self):
        return f"<ServiceResponse(success={self.status}, data={self.data}, error={self.error})>"

    def to_dict(self, non_null=False):
        return {k: v for k, v in self.__dict__.items() if v is not None} if non_null else self.__dict__

    def __bool__(self):
        return self.status

    def __str__(self):
        return f"{self.status}"
