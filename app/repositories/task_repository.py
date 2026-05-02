from uuid import UUID, uuid4
from datetime import datetime, timezone
from typing import List, Optional, Dict
from app.models.task import TaskCreate, TaskUpdate, TaskOut

class TaskRepository:
    """
    Abstração para persistência de dados de tarefas.
    Implementa um armazenamento em memória funcional para o CRUD.
    """
    
    def __init__(self):
        # Armazenamento volátil para simular um banco de dados
        self._storage: Dict[UUID, TaskOut] = {}

    def _generate_metadata(self) -> dict:
        """Centraliza a geração de campos controlados pelo sistema (DRY)."""
        now = datetime.now(timezone.utc)
        return {
            "id": uuid4(),
            "created_at": now,
            "updated_at": now
        }

    async def save(self, task_data: TaskCreate, priority_hint: Optional[str] = None) -> TaskOut:
        """Persiste uma nova tarefa, injetando metadados e prioridade sugerida."""
        metadata = self._generate_metadata()
        
        # Cria o objeto TaskOut combinando dados de entrada, metadados e a sugestão de prioridade
        task_dict = task_data.model_dump()
        if priority_hint and not task_dict.get("priority"):
            task_dict["priority"] = priority_hint
            
        task = TaskOut(**metadata, **task_dict)
        self._storage[task.id] = task
        return task

    async def find_all(self) -> List[TaskOut]:
        """Retorna todas as tarefas armazenadas."""
        return list(self._storage.values())

    async def find_by_id(self, task_id: UUID) -> Optional[TaskOut]:
        """Busca uma tarefa específica por ID."""
        return self._storage.get(task_id)

    async def update(self, task_id: UUID, task_data: TaskUpdate) -> Optional[TaskOut]:
        """Atualiza parcialmente uma tarefa existente."""
        task = await self.find_by_id(task_id)
        if not task:
            return None
        
        # Mescla dados existentes com novos dados (ignorando campos não enviados)
        update_data = task_data.model_dump(exclude_unset=True)
        updated_task = task.model_copy(update=update_data)
        updated_task.updated_at = datetime.now(timezone.utc)
        
        self._storage[task_id] = updated_task
        return updated_task

    async def delete(self, task_id: UUID) -> bool:
        """Remove uma tarefa e retorna sucesso."""
        if task_id in self._storage:
            del self._storage[task_id]
            return True
        return False
