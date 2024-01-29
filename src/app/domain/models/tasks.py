from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.schemas.tasks import GetTasks
from app.infrastructure.db import Base


class Task(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)

    def to_read_model(self) -> GetTasks:
        return GetTasks(id=self.id,
                        name=self.name,
                        description=self.description)
