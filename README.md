# Task Manager AI - Micro-API de Gerenciamento de Tarefas

Uma API RESTful desenvolvida com FastAPI para gerenciamento de tarefas, apresentando um diferencial de **Prioridade Assistida por IA**. O sistema analisa título e descrição para sugerir automaticamente a urgência da tarefa, utilizando uma abordagem híbrida (LLM com fallback para heurística local).

## 🚀 Arquitetura e Tecnologias

O projeto segue princípios de **Clean Architecture** e **SOLID**, garantindo baixo acoplamento e facilidade de teste:

- **FastAPI**: Framework web moderno e de alta performance.
- **Pydantic V2**: Validação de dados e definição de schemas.
- **Service Layer**: Lógica de negócio isolada para orquestração (TaskService).
- **Repository Pattern**: Abstração de persistência (atualmente In-Memory).
- **AI Priority Advisor**: Componente especializado em análise de prioridade via OpenAI/Heurísticas.

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.9+
- Pip (gerenciador de pacotes)

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd laboratorio-projeto
   ```

2. **Criar e ativar ambiente virtual:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # .venv\Scripts\activate   # Windows
   ```

3. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Variáveis de Ambiente (Opcional):**
   Para habilitar a sugestão via IA real, crie um arquivo `.env`:
   ```env
   OPENAI_API_KEY=sua_chave_aqui
   ```

## 🏃 Execução

Para iniciar o servidor de desenvolvimento:

```bash
uvicorn app.main:app --reload
```

Acesse a documentação interativa em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🧪 Testes

A suíte de testes utiliza **Pytest** e cobre serviços, rotas e lógica de IA:

```bash
# Executar todos os testes
pytest

# Executar com relatório de cobertura (se instalado)
pytest --cov=app tests/
```

## 🧠 Inteligência Artificial (Priority Advisor)

O sistema de prioridade opera em três níveis de confiança:
1. **LLM (OpenAI):** Tenta uma análise semântica profunda via API.
2. **Fallback (Timeout/Erro):** Se a API falhar ou demorar mais de 5s, o sistema aciona automaticamente a heurística local.
3. **Heurística Local:** Analisa palavras-chave (ex: "urgente", "erro", "amanhã") para determinar a prioridade sem custo ou latência externa.

## ⚠️ Limitações do MVP
- **Persistência Volátil:** Os dados são armazenados em memória e perdidos ao reiniciar o servidor.
- **Autenticação:** Não implementada nesta versão inicial.
- **Integração LLM:** Atualmente em modo de simulação/stub (implementação base presente).

## 🛤️ Próximos Passos
- [ ] Implementar persistência real com **SQLAlchemy** e SQLite/PostgreSQL.
- [ ] Adicionar suporte a **Tags** e Categorias.
- [ ] Implementar **JWT Authentication**.
- [ ] Dashboard de visualização de tarefas por prioridade.

---

## 🔍 Checklist Técnico e Evolução

### **Riscos Técnicos Restantes**
* **Volatilidade de Dados:** O repositório é instanciado a cada requisição no `task_routes.py`, fazendo com que os dados sejam perdidos imediatamente após cada chamada HTTP (falta de Singleton/Injeção persistente).
* **API "Invisível":** O arquivo `app/main.py` ainda não registra o roteador de tarefas, impedindo o acesso aos endpoints via servidor Uvicorn.
* **Concorrência:** O armazenamento em `dict` não é thread-safe para operações assíncronas simultâneas em produção.
* **Stub de IA:** O `PriorityAdvisor` utiliza um stub; a integração real com LangChain/OpenAI ainda não foi finalizada.

### **Gaps de Cobertura de Teste**
* **Validação de Models:** Testar restrições do Pydantic (ex: títulos vazios ou status inválidos).
* **Persistência entre Chamadas:** Validar se uma tarefa criada via POST permanece disponível em GETs subsequentes.
* **Captura de Logs:** Corrigir a propagação de logs para validação de fallbacks nos testes assíncronos.

### **Melhorias Prioritárias (Próxima Release)**
* **Injeção de Singleton:** Garantir instância única do repositório no ciclo de vida da API.
* **Registro de Rotas:** Conectar o roteador ao arquivo principal `main.py`.
* **Banco de Dados:** Migrar para **SQLite** utilizando **SQLModel**.
* **Middleware de Erros:** Implementar handlers globais para exceções padronizadas.

