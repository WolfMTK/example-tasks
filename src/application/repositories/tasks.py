from src.application.protocols.repository import SQLAlchemyRepository
from src.domain.models.tasks import Task


class TasksRepository(SQLAlchemyRepository):
    model = Task
