from typing import List, Dict

from domain.tasks.entities.task import Task
from domain.tasks.interfaces.task_repo import ITaskRepo


class InmemoryTaskRepo(ITaskRepo):
    _task_list: Dict[int, Task] = {}
    _last_id = 0

    def delete_by_id(self, id_: int) -> Task:
        return self._task_list.pop(id_, None)

    def get_by_id(self, id_: int) -> Task:
        return self._task_list.get(id_)

    def get_tasks(self) -> List[Task]:
        return list(self._task_list.values())

    def add_task(self, task: Task) -> None:
        self._last_id += 1
        task.id_ = self._last_id
        self._task_list[self._last_id] = task

    def checkpoint_trigger(self, task: Task) -> bool:
        return not task