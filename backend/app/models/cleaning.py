from typing import Optional
from enum import Enum

from app.models.core import IDModelMixin, CoreModel


class CleaningType(str, Enum):
    dust_up = "dust_up"
    spot_clean = "spot_clean"
    full_clean = "full_clean"


class CleaningBase(CoreModel):
    """
    All common characteristics of our Cleaning resource
    """
    name: str | None = None
    description: str | None = None
    price: float | None = None
    cleaning_type: CleaningType | None = "spot_clean"


class CleaningCreate(CleaningBase):
    name: str
    price: float


class CleaningUpdate(CleaningBase):
    cleaning_type: CleaningType | None = None


class CleaningInDB(IDModelMixin, CleaningBase):
    name: str
    price: float
    cleaning_type: CleaningType


class CleaningPublic(IDModelMixin, CleaningBase):
    pass