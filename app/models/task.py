from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field

class TaskBase(SQLModel):
    """Modelo base para tarefas compartilhando campos comuns."""
    title: str = Field(index=True, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    status: str = Field(default="pending")
    priority: Optional[str] = Field(default=None)

class Task(TaskBase, table=True):
    """Definição da tabela de tarefas no banco de dados."""
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class TaskCreate(TaskBase):
    """Modelo para criação de novas tarefas."""
    pass

class TaskUpdate(SQLModel):
    """Modelo para atualização parcial de tarefas."""
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None

class TaskOut(TaskBase):
    """Modelo para retorno de dados da tarefa."""
    id: UUID
    created_at: datetime
    updated_at: datetime
