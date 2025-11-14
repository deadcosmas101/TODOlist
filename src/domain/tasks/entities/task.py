import attr


@attr.dataclass
class Task:
    user_task: str
    user_checkpoint: bool
    id_: int | None = None
