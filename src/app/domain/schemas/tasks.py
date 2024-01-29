from pydantic import BaseModel, Field, ConfigDict


class BaseTasks(BaseModel):
    name: str | None = Field(None, max_length=50)
    description: str | None = Field(None)


class CreateTasks(BaseTasks):
    name: str


class UpdateTasks(BaseTasks):
    name: str | None = None
    description: str | None = None


class GetTasks(BaseTasks):
    id: int
