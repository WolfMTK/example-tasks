from fastapi import APIRouter

from src.domain.schemas.tasks import CreateTasks, GetTasks, UpdateTasks
from src.application.services.tasks import TasksService


from .dependencies import UoWDep

router = APIRouter(prefix='/tasks', tags=['tasks'])


@router.post('/', response_model=GetTasks, response_model_exclude_none=True)
async def create_task(uow: UoWDep, task: CreateTasks):
    return await TasksService().create_task(uow, task)


@router.get('/', response_model=list[GetTasks], response_model_exclude_none=True)
async def get_tasks(uow: UoWDep):
    return await TasksService().get_tasks(uow)


@router.patch('/{id}', response_model=GetTasks,
              response_model_exclude_none=True)
async def update_task(id: int, task: UpdateTasks, uow: UoWDep):
    return await TasksService().update_task(uow, id, task)


@router.get('/{id}', response_model=GetTasks,
            response_model_exclude_none=True)
async def get_task(id: int, uow: UoWDep):
    return await TasksService().get_task(uow, id)


@router.delete('/{id}', response_model=GetTasks,
               response_model_exclude_none=True)
async def delete_task(id: int, uow: UoWDep):
    return await TasksService().delete_task(uow, id)
