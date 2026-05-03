# Task Manager AI - Micro-API de Gerenciamento de Tarefas

[![Changelog](https://img.shields.io/badge/changelog-v0.2.0-blue)](CHANGELOG.md)

Uma API RESTful desenvolvida com FastAPI para gerenciamento de tarefas, apresentando um diferencial de **Prioridade Assistida por IA**. O sistema analisa título e descrição para sugerir automaticamente a urgência da tarefa, utilizando uma abordagem híbrida (LLM com fallback para heurística local).

## 🚀 Arquitetura e Tecnologias

O projeto segue princípios de **Clean Architecture** e **SOLID**, garantindo baixo acoplamento e facilidade de teste. Para uma visão detalhada, consulte nosso [Documento de Arquitetura](docs/arquitetura.md).

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
   git clone git@github.com:rodrigoferrazazevedo/ufg-todo-list.git
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
```

## 🧠 Inteligência Artificial (Priority Advisor)

O sistema de prioridade opera em três níveis de confiança. Detalhes sobre o planejamento podem ser vistos no [Documento de Escopo](docs/escopo-mvp.md).

1. **LLM (OpenAI):** Tenta uma análise semântica profunda via API.
2. **Fallback (Timeout/Erro):** Se a API falhar ou demorar mais de 5s, o sistema aciona automaticamente a heurística local.
3. **Heurística Local:** Analisa palavras-chave para determinar a prioridade sem custo ou latência externa.

## ⚠️ Limitações do MVP
- **Persistência Volátil:** Os dados são armazenados em memória e perdidos ao reiniciar o servidor.
- **Autenticação:** Não implementada nesta versão inicial.

## 🛤️ Próximos Passos

O acompanhamento detalhado da evolução do projeto pode ser feito através do nosso [Backlog Completo](docs/backlog.md).

- [ ] Implementar persistência real com **SQLite** e **SQLModel**.
- [ ] Adicionar suporte a **Filtros** na listagem de tarefas.
- [ ] Implementar **JWT Authentication**.
- [ ] Dashboard de visualização de tarefas por prioridade.

---

## 🔍 Checklist Técnico e Evolução

### **Riscos Técnicos Restantes**
* **Concorrência:** O armazenamento em SQLite/SQLModel deve ser monitorado para garantir performance em múltiplos acessos simultâneos (embora o SQLite lide bem com acessos sequenciais).
* **Stub de IA:** O `PriorityAdvisor` utiliza um stub; a integração real com LangChain/OpenAI ainda não foi finalizada.

### **Gaps de Cobertura de Teste**
* **Validação de Models:** Testar restrições do Pydantic (ex: títulos vazios ou status inválidos).
* **Migrações de Banco:** Implementar testes para garantir integridade em futuras mudanças de esquema (ex: usando Alembic).
* **Captura de Logs:** Corrigir a propagação de logs para validação de fallbacks nos testes assíncronos.

### **Melhorias Concluídas (Release Atual)**
* ✅ **Persistência Real:** Implementação de **SQLite** com **SQLModel**.
* ✅ **Integração de Rotas:** Registro completo do roteador no `main.py`.
* ✅ **Inicialização Automática:** Criação de tabelas no startup da API.

### **Melhorias Prioritárias (Próxima Release)**
* **Middleware de Erros:** Implementar handlers globais para exceções padronizadas.
* **Autenticação:** Implementar fluxo JWT.


---

## 🤖 Assistência de IA

Este projeto foi desenvolvido com o suporte da Inteligência Artificial (Gemini CLI), atuando como parceiro de programação sênior.

**Destaques da Colaboração:**
*   **Refatoração Arquitetural:** Aplicação de padrões de projeto (Repository, Service Layer) e princípios SOLID.
*   **QA Automatizado:** Geração de suíte de testes completa com cobertura de serviços, rotas e lógica de IA.
*   **Documentação Contínua:** Manutenção sincronizada de diagramas, backlog e análise de riscos técnicos.
*   **Debugging Proativo:** Resolução de conflitos de ambiente e logs assíncronos.

Consulte o [Relato Completo de Assistência de IA](docs/relatorio-ia.md) para mais detalhes sobre a metodologia utilizada.


