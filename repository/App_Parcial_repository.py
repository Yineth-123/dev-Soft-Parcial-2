from abc import ABC, abstractmethod
from typing import List, Optional
from App_Parcial.model.App_Parcial import Task
from App_Parcial.enums import TaskStatus

class ITaskRepository(ABC):

    @abstractmethod
    def save(self, task: Task) -> Task:
        pass

    @abstractmethod
    def find_all(self, status: Optional[TaskStatus] = None) -> List[Task]:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Task]:
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        pass

    @abstractmethod
    def find_overdue(self) -> List[Task]:
        pass
