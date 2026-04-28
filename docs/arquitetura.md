# Arquitetura de Componentes

Diagrama representativo das camadas da API e o fluxo de interação entre os componentes e serviços externos.

```mermaid
graph LR
    subgraph Client_Layer [Client]
        User((Usuário/Frontend))
    end

    subgraph API_Layer [Camada de API]
        Endpoints[FastAPI Endpoints]
    end

    subgraph Service_Layer [Camada de Serviço]
        TaskService[TaskService]
    end

    subgraph Component_Layer [Componentes AI]
        PriorityAdvisor[PriorityAdvisor]
    end

    subgraph Data_Layer [Camada de Dados]
        Repository[TaskRepository]
        DB[(SQLite)]
    end

    subgraph External_Layer [Externo]
        LLM[OpenAI/LangChain]
    end

    %% Fluxos de Dados
    User -->|Request| Endpoints
    Endpoints -->|Call| TaskService
    
    TaskService -->|CRUD Ops| Repository
    TaskService -->|Análise| PriorityAdvisor
    
    Repository -->|Query/Persist| DB
    PriorityAdvisor -->|Prompt/Analysis| LLM
    
    TaskService -->|Response Data| Endpoints
    Endpoints -->|JSON Response| User
```

## Descrição das Camadas
- **API Layer**: Gerencia as rotas, validações de entrada (Pydantic) e serialização de saída.
- **Service Layer**: Contém a lógica de negócio e orquestra a interação entre o repositório e os componentes de IA.
- **PriorityAdvisor**: Especialista em interagir com LLMs para extrair insights de priorização das tarefas.
- **Data Layer**: Abstrai o acesso ao banco de dados SQLite utilizando o padrão Repository.
