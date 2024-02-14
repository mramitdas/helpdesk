from datetime import date

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


class BaseUser(UUIDMixin, TimestampMixin):
    """
    BaseUser class representing a user with UUID, timestamps, and basic user information.

    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (EmailStr): The email address of the user.
        phone_no (str): The phone number of the user.
        gender (str): The gender of the user. Default is an empty string.
        address (str): The user's address.
        city (str): The user's city.
        country (str): The user's country.
        zip_code (str): The user's zip code.
        date_of_birth (date): The user's date of birth.
        is_active (bool): Indicates if the user account is active. Default is True.
    """

    first_name: str = Field(
        default=None, title="First Name", description="The first name of the user"
    )
    last_name: str = Field(
        default=None, title="Last Name", description="The last name of the user"
    )
    email: EmailStr = Field(
        default=None, title="Email", description="The email address of the user"
    )
    phone_no: str = Field(
        default=None, title="Phone Number", description="The phone number of the user"
    )
    gender: str = Field(
        default=None, title="Gender", description="The gender of the user"
    )
    address: str = Field(
        default=None, title="Address", description="The user's address"
    )
    city: str = Field(default=None, title="City", description="The user's city")
    country: str = Field(
        default=None, title="Country", description="The user's country"
    )
    zip_code: str = Field(
        default=None, title="Zip Code", description="The user's zip code"
    )
    date_of_birth: date = Field(
        default=None, title="Date of Birth", description="The user's date of birth"
    )
    is_active: bool = Field(
        default=True,
        title="Active",
        description="Indicates if the user account is active",
    )


class Customer(BaseUser, UserPerm):
    """
    Customer class representing a customer with inherited basic user information.

    Inherits from BaseUser class.
    """


class SupportPerson(BaseUser, UserPerm):
    """
    SupportPerson class representing a support person with inherited basic user information and permissions.

    Inherits from BaseUser and UserPerm classes.

    Attributes:
        is_sp (bool): Indicates if the user is a support person. Default is True.
    """

    is_sp: bool = Field(
        default=True,
        title="Support User",
        description="Indicates if the user is a support person (Service Provider)",
    )


class Admin(BaseUser, UserPerm):
    """
    Admin class representing an admin with inherited basic user information and permissions.

    Inherits from BaseUser and UserPerm classes.

    Attributes:
        is_admin (bool): Indicates if the user is an admin. Default is True.
    """

    is_admin: bool = Field(
        default=True,
        title="Admin User",
        description="Indicates if the user is an admin",
    )


class SuperUser(BaseUser, UserPerm):
    """
    SuperUser class representing a superuser with inherited basic user information and permissions.

    Inherits from BaseUser and UserPerm classes.
    """

    is_superuser: bool = Field(
        default=True,
        title="Superuser",
        description="Indicates if the user is a superuser",
    )
