from datetime import datetime
from typing import Optional

import pytz
from pydantic import BaseModel, Field


class TimestampMixin(BaseModel):
    """
    A Pydantic mixin class to provide timestamp fields for created and updated times.

    This mixin class extends Pydantic's `BaseModel` to include timestamp fields for both 'created_at' and 'updated_at' times. The timestamps are automatically generated in the 'Asia/Kolkata' timezone when an instance of a model that inherits from this mixin is created.

    Attributes:
        created_at (datetime): The timestamp indicating the creation time of the object.
        updated_at (Optional[datetime]): The timestamp indicating the last update time of the object. It is set to `None` initially.

    Note:
        - The timestamps are generated in the 'Asia/Kolkata' timezone.
        - The default format for the timestamps is '%Y-%m-%d %H:%M:%S.%f'.
    """

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(pytz.timezone("Asia/Kolkata"))
    )
    updated_at: Optional[datetime] = None
