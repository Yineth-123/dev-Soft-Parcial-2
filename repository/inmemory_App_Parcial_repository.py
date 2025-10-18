from typing import List, Optional
from datetime import datetime
from App_Parcial.model.App_Parcial import Task
from App_Parcial.enums import TaskStatus
from App_Parcial.repository.App_Parcial_repository import ITaskRepository

class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self.store: List[Task] = []

    def save(self, task: Task) -> Task:
        self.store.append(task)
        return task

    def find_all(self, status: Optional[TaskStatus] = None) -> List[Task]:
        if status:
            return [task for task in self.store if task.status == status]
        return list(self.store)

    def find_by_id(self, id: int) -> Optional[Task]:
        return next((task for task in self.store if task.id == id), None)

    def delete(self, id: int) -> bool:
        task = self.find_by_id(id)
        if task:
            self.store.remove(task)
            return True
        return False

    def find_overdue(self) -> List[Task]:
        now = datetime.utcnow()
        return [
            task for task in self.store
            if task.due_date is not None and task.due_date < now and task.status != TaskStatus.DONE
        ]
