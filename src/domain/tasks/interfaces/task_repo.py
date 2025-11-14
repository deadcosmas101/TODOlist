from abc import ABC, abstractmethod
from typing import List

from domain.tasks.entities.task import Task


class ITaskRepo(ABC):
    @abstractmethod
    def add_task(self, task: Task) -> None:
        ...

    @abstractmethod
    def get_tasks(self) -> List[Task]:
        ...

    @abstractmethod
    def get_by_id(self, id_: int) -> Task:
        ...

    @abstractmethod
    def delete_by_id(self, id_: int) -> Task:
        pass
