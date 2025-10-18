from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from App_Parcial.dto.App_Parcial_create_dto import TaskCreateDTO
from App_Parcial.dto.App_Parcial_update_status_dto import TaskUpdateStatusDTO
from App_Parcial.dto.App_Parcial_dto import TaskDTO
from App_Parcial.service.App_Parcial_service import TaskService
from App_Parcial.repository.inmemory_App_Parcial_repository import InMemoryTaskRepository
from App_Parcial.enums import TaskStatus

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# Instanciamos repo y service (in-memory según diagrama)
repo = InMemoryTaskRepository()
service = TaskService(repo)

@router.post("", response_model=TaskDTO, status_code=201)
def create_task(payload: TaskCreateDTO):
    try:
        task = service.create(payload.title, payload.description, payload.due_date)
        return task
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=List[TaskDTO])
def list_tasks(status: Optional[TaskStatus] = Query(None, description="Filtrar por estado")):
    # FastAPI convertirá el query param al enum si coincide
    return service.list(status)

@router.get("/overdue", response_model=List[TaskDTO])
def overdue_tasks():
    return service.list_overdue()

@router.patch("/{task_id}/status", response_model=TaskDTO)
def update_status(task_id: int, payload: TaskUpdateStatusDTO):
    try:
        return service.update_status(task_id, payload.status)
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    try:
        service.delete(task_id)
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))
