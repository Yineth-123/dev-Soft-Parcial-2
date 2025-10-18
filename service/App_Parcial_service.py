from datetime import datetime
from typing import Optional, List
from App_Parcial.model.App_Parcial import Task
from App_Parcial.enums import TaskStatus
from App_Parcial.repository.App_Parcial_repository import ITaskRepository

class TaskService:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    def create(self, title: str, description: Optional[str], due_date: Optional[datetime]) -> Task:
        if not title or not title.strip():
            raise ValueError("El título es obligatorio")
        if due_date and due_date < datetime.utcnow():
            raise ValueError("La fecha no puede ser en el pasado")
        task = Task(title=title.strip(), description=description, due_date=due_date)
        return self.repository.save(task)

    def list(self, status: Optional[TaskStatus] = None) -> List[Task]:
        return self.repository.find_all(status)

    def update_status(self, id: int, status: TaskStatus) -> Task:
        task = self.repository.find_by_id(id)
        if not task:
            raise LookupError("Tarea no encontrada")
        # validación simple de transición (opcional)
        task.status = status
        return task

    def delete(self, id: int):
        if not self.repository.delete(id):
            raise LookupError("Tarea no encontrada")

    def list_overdue(self) -> List[Task]:
        return self.repository.find_overdue()
