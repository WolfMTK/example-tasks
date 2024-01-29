from app.application.protocols.repository import SQLAlchemyRepository
from app.domain.models.tasks import Task


class TasksRepository(SQLAlchemyRepository):
    model = Task
