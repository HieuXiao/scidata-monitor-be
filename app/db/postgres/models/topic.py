
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.postgres.base import Base


class TopicCluster(Base):
    __tablename__ = "topic_clusters"

    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(String(255))
    keywords: Mapped[str] = mapped_column(String(1024))  # Comma separated keywords

class TopicAssignment(Base):
    __tablename__ = "topic_assignments"

    paper_id: Mapped[int] = mapped_column(ForeignKey("papers.id"), primary_key=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topic_clusters.id"), primary_key=True)
    score: Mapped[float] = mapped_column(nullable=True)
