from pydantic import BaseModel

class Error(BaseModel):
    """
    Represents an error with a code and a descriptive message.

    Attributes:
        code (int): The error code indicating the type of error.
        message (str): A human-readable error message explaining the issue.
    """
    code: int
    message: str
    