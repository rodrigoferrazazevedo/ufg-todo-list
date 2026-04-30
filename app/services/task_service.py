from uuid import UUID
from typing import List, Optional
from app.models.task import TaskCreate, TaskUpdate, TaskOut
from app.repositories.task_repository import TaskRepository

class TaskService:
    """
    Serviço que gerencia a lógica de negócio das tarefas.
    Faz a ponte entre a API, o Repositório e o PriorityAdvisor.
    """
    
    def __init__(self, repository: TaskRepository, priority_advisor):
        """
        Inicializa o serviço com suas dependências.
        
        :param repository: Instância de TaskRepository para persistência.
        :param priority_advisor: Componente de IA para sugestão de prioridades.
        """
        self.repository = repository
        self.priority_advisor = priority_advisor

    async def create_task(self, task_data: TaskCreate) -> TaskOut:
        """
        Cria uma nova tarefa, integrando a sugestão automática de prioridade.
        """
        # Solicita sugestão de prioridade baseada no título e descrição
        suggestion = await self.priority_advisor.suggest_priority(
            title=task_data.title,
            description=task_data.description
        )
        
        # Aqui a regra de negócio poderia injetar a sugestão nos metadados 
        # ou campos específicos antes de salvar via repositório
        return await self.repository.save(task_data, priority_hint=suggestion)

    async def get_all_tasks(self) -> List[TaskOut]:
        """Recupera todas as tarefas do repositório."""
        return await self.repository.find_all()

    async def get_task_by_id(self, task_id: UUID) -> Optional[TaskOut]:
        """Busca uma tarefa pelo seu identificador único."""
        return await self.repository.find_by_id(task_id)

    async def update_task(self, task_id: UUID, task_data: TaskUpdate) -> Optional[TaskOut]:
        """Aplica atualizações em uma tarefa existente."""
        return await self.repository.update(task_id, task_data)

    async def delete_task(self, task_id: UUID) -> bool:
        """Remove uma tarefa e retorna True se a operação foi bem sucedida."""
        return await self.repository.delete(task_id)
