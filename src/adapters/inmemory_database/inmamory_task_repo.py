from typing import List

from domain.tasks.entities.task import Task
from domain.tasks.interfaces.task_repo import ITaskRepo


class InmemoryTaskRepo(ITaskRepo):
    def get_tasks(self) -> List[Task]:
        return self._task_list

    _task_list: List[Task] = []

    def add_task(self, task: Task) -> None:
        self._task_list.append(task)
