from uuid import UUID
from datetime import datetime, timezone
from typing import List, Optional
from sqlmodel import Session, select
from app.models.task import Task, TaskCreate, TaskUpdate, TaskOut

class TaskRepository:
    """
    Abstração para persistência de dados de tarefas utilizando SQLModel.
    """
    
    def __init__(self, session: Session):
        self.session = session

    async def save(self, task_data: TaskCreate, priority_hint: Optional[str] = None) -> TaskOut:
        """Persiste uma nova tarefa no SQLite."""
        task_dict = task_data.model_dump()
        
        # Injeta prioridade sugerida se não fornecida manualmente
        if priority_hint and not task_dict.get("priority"):
            task_dict["priority"] = priority_hint
            
        db_task = Task(**task_dict)
        self.session.add(db_task)
        self.session.commit()
        self.session.refresh(db_task)
        return TaskOut.model_validate(db_task)

    async def find_all(self) -> List[TaskOut]:
        """Retorna todas as tarefas persistidas."""
        statement = select(Task)
        results = self.session.exec(statement).all()
        return [TaskOut.model_validate(task) for task in results]

    async def find_by_id(self, task_id: UUID) -> Optional[TaskOut]:
        """Busca uma tarefa específica por ID."""
        db_task = self.session.get(Task, task_id)
        return TaskOut.model_validate(db_task) if db_task else None

    async def update(self, task_id: UUID, task_data: TaskUpdate) -> Optional[TaskOut]:
        """Atualiza parcialmente uma tarefa no banco de dados."""
        db_task = self.session.get(Task, task_id)
        if not db_task:
            return None
        
        # Atualiza campos fornecidos
        task_data_dict = task_data.model_dump(exclude_unset=True)
        for key, value in task_data_dict.items():
            setattr(db_task, key, value)
        
        db_task.updated_at = datetime.now(timezone.utc)
        self.session.add(db_task)
        self.session.commit()
        self.session.refresh(db_task)
        return TaskOut.model_validate(db_task)

    async def delete(self, task_id: UUID) -> bool:
        """Remove uma tarefa do banco de dados."""
        db_task = self.session.get(Task, task_id)
        if not db_task:
            return False
        
        self.session.delete(db_task)
        self.session.commit()
        return True
