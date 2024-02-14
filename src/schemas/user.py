from pydantic import BaseModel, EmailStr, Field

from .utils import TimestampMixin, UUIDMixin


class UserPerm(BaseModel):
    """
    UserPerm class representing user permissions.

    Attributes:
        is_superuser (bool): Indicates if the user is a superuser. Default is False.
        is_admin (bool): Indicates if the user is an admin. Default is False.
        is_sp (bool): Indicates if the user is an SP (Service Provider). Default is False.
    """

    is_superuser: bool = Field(
        default=False,
        title="Superuser",
        description="Indicates if the user is a superuser",
    )
    is_admin: bool = Field(
        default=False, title="Admin", description="Indicates if the user is an admin"
    )
    is_sp: bool = Field(
        default=False,
        title="Support User",
        description="Indicates if the user is an SP (Service Provider)",
    )
