import attr


@attr.dataclass
class Task():
    user_task: str
    user_chekpoint: bool
    