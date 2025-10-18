from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreateDTO(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
