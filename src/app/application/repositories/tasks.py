from app.application.protocols.repository import SQLAlchemyRepository
from src.app.domain.models.tasks import Task


class TasksRepository(SQLAlchemyRepository):
    model = Task
