from datetime import datetime
from pydantic import BaseModel, validator


class CoreModel(BaseModel):
    """
    Any commnon logic to be shared by all models goes here
    """
    pass


class IDModelMixin(BaseModel):
    id: int


class DateTimeModelMixin(BaseModel):
    created_at: datetime | None = None
    updated_at: datetime | None = None

    @validator("created_at", "updated_at", pre=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()