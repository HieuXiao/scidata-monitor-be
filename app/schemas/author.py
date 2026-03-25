
from pydantic import BaseModel, ConfigDict


class AuthorBase(BaseModel):
    name: str
    orcid: str | None = None
    affiliation_id: int | None = None

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(AuthorBase):
    name: str | None = None

class AuthorInDBBase(AuthorBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class Author(AuthorInDBBase):
    pass
