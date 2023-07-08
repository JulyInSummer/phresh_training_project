from pydantic import BaseModel


class CoreModel(BaseModel):
    """
    Any commnon logic to be shared by all models goes here
    """
    pass


class IDModelMixin(BaseModel):
    id: int