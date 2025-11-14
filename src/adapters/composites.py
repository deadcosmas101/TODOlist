from src.adapters.inmemory_database.inmamory_task_repo import InmemoryTaskRepo
from src.domain.tasks.services.task_service import TaskService


def create_inmemory_task_repo() -> InmemoryTaskRepo:
    return InmemoryTaskRepo()

def create_task_service() -> TaskService:
    return TaskService(create_inmemory_task_repo())


