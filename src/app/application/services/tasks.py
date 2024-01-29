from app.application.protocols.unit_of_work import UoW
from app.domain.schemas.tasks import CreateTasks, UpdateTasks, GetTasks


class TasksService:
    async def get_tasks(self, uow: UoW) -> list[GetTasks]:
        async with uow:
            tasks = await uow.tasks.find_all()
            return [task.to_read_model() for task in tasks]

    async def get_task(self, uow: UoW, id: int) -> GetTasks:
        async with uow:
            task = await uow.tasks.find_one(id=id)
            return task.to_read_model()

    async def create_task(self, uow: UoW, schema: CreateTasks) -> GetTasks:
        async with uow:
            task = await uow.tasks.add_one(**schema.model_dump())
            await uow.commit()
            return task.to_read_model()

    async def update_task(self, uow: UoW, id: int,
                          schema: UpdateTasks) -> GetTasks:
        async with uow:
            task = await uow.tasks.update_one(id=id, **schema.model_dump())
            await uow.commit()
            print(task.to_read_model())
            return task.to_read_model()

    async def delete_task(self, uow: UoW, id: int) -> GetTasks:
        async with uow:
            task = await uow.tasks.delete_one(id=id)
            await uow.commit()
            return task.to_read_model()
