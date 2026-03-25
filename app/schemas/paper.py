from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PaperBase(BaseModel):
    doi: str | None = None
    title: str
    abstract: str | None = None
    publication_year: int
    source: str
    source_id: str

class PaperCreate(PaperBase):
    pass

class PaperUpdate(PaperBase):
    title: str | None = None
    publication_year: int | None = None
    source: str | None = None
    source_id: str | None = None

class PaperInDBBase(PaperBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class Paper(PaperInDBBase):
    pass
