import TaskManagerCLI.Task as task
import argparse

class Service:
    def __init__(self, AC):
        self.endpoints = AC.Endpoints
        self.current_task = None

    def add_task(self, name: str):
        self.current_task = task.Task(name)
        self.endpoints.LinkedList.append(self.current_task)

    def update_task(self, name_old, name_new):
        self.endpoints.LinkedList.update(name_old, task.Task(name_new))

    def delete_task(self, name):
        self.endpoints.LinkedList.remove(name)

    def mark_task(self, name: str, status_update: int):
        node = self.endpoints.LinkedList.head
        while node is not None:
            if node.value.name == name:
                node.value.status = status_update
                break
            node = node.next













