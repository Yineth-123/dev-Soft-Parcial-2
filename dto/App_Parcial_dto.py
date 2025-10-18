from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from App_Parcial.enums import TaskStatus

class TaskDTO(BaseModel):
    id: int
    title: str
    description: Optional[str]
    due_date: Optional[datetime]
    status: TaskStatus
    created_at: datetime

    class Config:
        orm_mode = True
