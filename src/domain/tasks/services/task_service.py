from typing import List

import attr

from domain.tasks.interfaces.task_repo import ITaskRepo
from src.domain.tasks.entities.task import Task


@attr.frozen
class TaskService:
    task_repo: ITaskRepo

    def add_task(self, task: Task):
        self.task_repo.add_task(task)

    def get_tasks(self) -> List[Task]:
        return self.task_repo.get_tasks()
