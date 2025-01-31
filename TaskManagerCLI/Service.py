import Task
import argparse

class Service:
    def __init__(self, AC):
        self.endpoints = AC.Endpoints

    def add_task(self, name: str):
        self.endpoints.TaskList.append(Task.Task(name))

    def update_task(self, name_old, name_new):
        for task in self.endpoints.TaskList:
            if task.name == name_old:
                task.name = name_new
                print(f'Task name {name_old} was successfully updated to {task.name}.')
            else:
                print("Task name not found.")

    def delete_task(self, name):
        for task in self.endpoints.TaskList:
            if task.name == name:
                print(f'Task named: {task.name} was deleted successfully')
                task.pop()
            else:
                print("Task name not found.")

    def mark_task(self, name: str, status_update: int):
        try:
            for task in self.endpoints.TaskList:
                if task.name == name:
                    task.status = status_update
                    print(f"Task marked as {task.status.strip()}")
        except TypeError:
            print(f"{TypeError} in mark_task\nPlease don't fuck it up next time")

        finally:
            print("Mark_Task reached finally")











