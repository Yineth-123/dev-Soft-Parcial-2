from datetime import datetime
from App_Parcial.enums import TaskStatus

class Task:
    _id_counter = 1

    def __init__(self, title: str, description: str = None, due_date: datetime = None):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = TaskStatus.PENDING
        self.created_at = datetime.utcnow()
