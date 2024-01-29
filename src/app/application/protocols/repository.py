from abc import ABC, abstractmethod
from typing import TypeVar, Sequence, Any

from sqlalchemy import insert, select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.infrastructure.db import Base

ModelType = TypeVar('ModelType', bound=Base)


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self): ...

    @abstractmethod
    async def find_one(self): ...

    @abstractmethod
    async def find_all(self): ...

    @abstractmethod
    async def delete_one(self): ...


class SQLAlchemyRepository(AbstractRepository):
    model: ModelType | None = None

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add_one(self,
                      **kwargs: dict[str, Any]) -> ModelType:
        stmt = insert(self.model).values(**kwargs).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def update_one(self,
                         id: int,
                         **kwargs: dict[str, Any]) -> ModelType:
        stmt = update(self.model).values(**kwargs).filter_by(id=id).returning(
            self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def find_one(self, **filter_by: dict[str, Any]) -> ModelType | None:
        stmt = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def find_all(self) -> Sequence[ModelType]:
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def delete_one(self, **filter_by: dict[str, Any]) -> ModelType:
        stmt = delete(self.model).filter_by(**filter_by).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one()
