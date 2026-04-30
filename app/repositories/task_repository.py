from uuid import UUID, uuid4
from datetime import datetime
from typing import List, Optional
from app.models.task import TaskCreate, TaskUpdate, TaskOut

class TaskRepository:
    """
    Abstração para persistência de dados de tarefas.
    Implementa o padrão Repository para isolar a lógica de dados.
    """
    
    async def save(self, task_data: TaskCreate, priority_hint: Optional[str] = None) -> TaskOut:
        """Persiste uma nova tarefa no banco de dados."""
        # TODO: Implementar persistência real (SQLAlchemy/SQLite)
        return TaskOut(
            id=uuid4(),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            **task_data.model_dump()
        )

    async def find_all(self) -> List[TaskOut]:
        """Retorna todas as tarefas persistidas."""
        return []

    async def find_by_id(self, task_id: UUID) -> Optional[TaskOut]:
        """Busca uma tarefa específica por ID."""
        return None

    async def update(self, task_id: UUID, task_data: TaskUpdate) -> Optional[TaskOut]:
        """Atualiza uma tarefa no banco de dados."""
        return None

    async def delete(self, task_id: UUID) -> bool:
        """Remove uma tarefa do banco de dados."""
        return True
