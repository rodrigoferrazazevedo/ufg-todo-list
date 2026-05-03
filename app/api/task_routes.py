from uuid import UUID
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.models.task import TaskCreate, TaskUpdate, TaskOut
from app.services.task_service import TaskService
from app.repositories.task_repository import TaskRepository
from app.services.priority_advisor import PriorityAdvisor
from app.database import get_session

router = APIRouter(prefix="/tasks", tags=["tasks"])

def get_task_service(session: Session = Depends(get_session)):
    repo = TaskRepository(session)
    advisor = PriorityAdvisor()
    return TaskService(repo, advisor)

@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate, service: TaskService = Depends(get_task_service)):
    """
    Cria uma nova tarefa no banco de dados SQLite.
    A prioridade é sugerida automaticamente pelo PriorityAdvisor (IA/Heurística) 
    caso não seja informada manualmente.
    """
    return await service.create_task(task)

@router.get("/", response_model=List[TaskOut])
async def list_tasks(service: TaskService = Depends(get_task_service)):
    """
    Recupera todas as tarefas persistidas no banco de dados.
    """
    return await service.get_all_tasks()

@router.get("/{task_id}", response_model=TaskOut)
async def get_task(task_id: UUID, service: TaskService = Depends(get_task_service)):
    """
    Busca uma tarefa específica pelo seu ID único (UUID).
    Retorna 404 se a tarefa não for encontrada.
    """
    task = await service.get_task_by_id(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Task with id {task_id} not found"
        )
    return task

@router.put("/{task_id}", response_model=TaskOut)
async def update_task(task_id: UUID, task: TaskUpdate, service: TaskService = Depends(get_task_service)):
    """
    Atualiza parcialmente os campos de uma tarefa existente.
    Metadados como 'updated_at' são atualizados automaticamente.
    """
    updated_task = await service.update_task(task_id, task)
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Task with id {task_id} not found"
        )
    return updated_task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: UUID, service: TaskService = Depends(get_task_service)):
    """
    Remove permanentemente uma tarefa do banco de dados SQLite.
    """
    success = await service.delete_task(task_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Task with id {task_id} not found"
        )
    return None
