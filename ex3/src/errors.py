from typing import Callable

from fastapi.requests import Request
from fastapi.responses import JSONResponse


class BooklyException(Exception):
    """This is the base class for all bookly errors."""

class InvalidToken(BooklyException):
    """User has provided an invalid or expired token"""

class RevokedToken(BooklyException):
    """User has provided a token thar has been revokerd"""

class AccessTokenRequired(BooklyException):
    """User has provided an access token when a refresh token is needed"""

class RefreshTokenRequired(BooklyException):
    """User has provided an access token when a refresh token is needed"""

class UserAlreadyExists(BooklyException):
    """User has provided an email for a user who exists during sign up."""

class InvalidCredentials(BooklyException):
    """User has provided wrong email or password during log in"""

class InsufficientPermission(BooklyException):
    """User does not have the neccessary permissions to perrrform an action."""

class ReviewNotFound(BooklyException):
    """Review Not found"""

class BookNotFound(BooklyException):
    """Book Not found"""

class TagNotFound(BooklyException):
    """Tag not found"""

class TagAlreadyExists(BooklyException):
    """Tag alreaady exists"""

class UserNotFound(BooklyException):
    """User Not found"""

class AccountNotVerified(BooklyException):
    """Account not yet verifeid"""


def create_exception_handler(
    status_code: int,
    initial_detail,
) -> Callable[[Request, Exception], JSONResponse]:

    async def exception_handler(request: Request, exc: BooklyException):
        return JSONResponse(
            content=initial_detail,
            status_code=status_code
        )

    return exception_handler
