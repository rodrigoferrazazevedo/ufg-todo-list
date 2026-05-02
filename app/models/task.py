from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, ConfigDict

class TaskBase(BaseModel):
    """Modelo base para tarefas."""
    title: str = Field(..., min_length=1, max_length=100, description="Título da tarefa")
    description: Optional[str] = Field(None, max_length=500, description="Descrição detalhada")
    status: str = Field("pending", pattern="^(pending|in_progress|completed)$", description="Status da tarefa")
    priority: Optional[str] = Field(None, description="Prioridade sugerida ou definida")

class TaskCreate(TaskBase):
    """Modelo para criação de novas tarefas."""
    pass

class TaskUpdate(BaseModel):
    """Modelo para atualização parcial de tarefas."""
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[str] = Field(None, pattern="^(pending|in_progress|completed)$")
    priority: Optional[str] = Field(None)

class TaskOut(TaskBase):
    """Modelo para retorno de dados da tarefa."""
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
