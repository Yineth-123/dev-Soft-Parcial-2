from pydantic import BaseModel
from App_Parcial.enums import TaskStatus

class TaskUpdateStatusDTO(BaseModel):
    status: TaskStatus
