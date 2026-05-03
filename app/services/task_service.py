from uuid import UUID
from typing import List, Optional
from app.models.task import TaskCreate, TaskUpdate, TaskOut
from app.repositories.task_repository import TaskRepository

class TaskService:
    """
    Serviço que orquestra a lógica de negócio das tarefas (SRP).
    Coordena o enriquecimento via IA e a persistência via repositório.
    """
    
    def __init__(self, repository: TaskRepository, priority_advisor):
        self.repository = repository
        self.priority_advisor = priority_advisor

    async def create_task(self, task_data: TaskCreate) -> TaskOut:
        """Cria tarefa enriquecida com sugestão automática de prioridade."""
        suggestion = await self.priority_advisor.suggest_priority(
            title=task_data.title,
            description=task_data.description
        )
        return await self.repository.save(task_data, priority_hint=suggestion)

    async def get_all_tasks(self, status: Optional[str] = None) -> List[TaskOut]:
        return await self.repository.find_all(status=status)

    async def get_task_by_id(self, task_id: UUID) -> Optional[TaskOut]:
        return await self.repository.find_by_id(task_id)

    async def update_task(self, task_id: UUID, task_data: TaskUpdate) -> Optional[TaskOut]:
        return await self.repository.update(task_id, task_data)

    async def delete_task(self, task_id: UUID) -> bool:
        return await self.repository.delete(task_id)
