from typing import List, TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.postgres.base import Base

if TYPE_CHECKING:
    from app.db.postgres.models.institution import Institution
    from app.db.postgres.models.paper import Paper


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True)
    orcid: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=True)
    affiliation_id: Mapped[int] = mapped_column(ForeignKey("institutions.id"), nullable=True)

    papers: Mapped[List["Paper"]] = relationship(
        secondary="paper_authors", back_populates="authors"
    )
    institution: Mapped["Institution"] = relationship(back_populates="authors")
