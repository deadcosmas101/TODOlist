import os
import sys

import attr

from domain.tasks.services.task_service import TaskService
from src.domain.tasks.entities.task import Task


@attr.frozen
class CLI:
    task_service: TaskService

    def add_task(self):
        user_task = input()
        self.task_service.add_task(Task(user_task, False))
        input("Нажмите любую кнопку, что бы продолжить ")

    def show_tasks(self):
        resalt = self.task_service.get_tasks()
        for task in resalt:
            print(f"{task.user_task} {task.user_chekpoint}")
        input("Нажмите любую кнопку, что бы продолжить ")

    def show_menu(self):
        # os.system("cls")
        print("╔" + "═" * 40 + "╗")
        print("║{:^38}║".format("📝  КРАСИВЫЙ TODO ЛИСТ  📝"))
        print("╚" + "═" * 40 + "╝")
        print("\n📌  Меню:")
        print("   [1] ➕ Добавить задачу")
        print("   [2] ✔ Отметить выполненной / невыполненной")
        print("   [3] ❌ Удалить задачу")
        print("   [4] 📝 Показать задачи")
        print("   [5] 🚪 Выход")
        print("─" * 44)

        match_pattern = {
            1: self.add_task,
            2: self.checkpoint,
            3: self.delete_task,
            4: self.show_tasks,
            5: sys.exit,
        }

        try:
            user_input = int(input())
        except ValueError:
            print("Только цифры")
            input()
            return

        if user_input not in range(1, 6):
            print("Такого пункта - нету")
            input()
            return

        match_pattern.get(user_input, print)()

    def delete_task(self):
        input("Нажмите любую кнопку, что бы продолжить ")

    def checkpoint(self):
        input("Нажмите любую кнопку, что бы продолжить ")
