from typing import List, TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.postgres.base import Base

if TYPE_CHECKING:
    from app.db.postgres.models.author import Author


class Institution(Base):
    __tablename__ = "institutions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True)
    ror_id: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=True)
    country: Mapped[str] = mapped_column(String(100), nullable=True)

    authors: Mapped[List["Author"]] = relationship(back_populates="institution")
