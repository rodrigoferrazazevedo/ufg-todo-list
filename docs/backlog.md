# Backlog - Task Manager AI

## ✅ Concluído (v0.1.0)
- [x] Setup inicial e Health Check.
- [x] CRUD completo de tarefas (Routes, Service, Repository).
- [x] Lógica de IA híbrida (PriorityAdvisor) com Fallback Local.
- [x] Cobertura de testes automatizados (Pytest).
- [x] Refatoração SRP/DRY do repositório e serviços.

## 🏁 Milestone 1: Data Persistence & Integration (v0.2.0)
- [ ] **Registro Global de Rotas**: Conectar `task_routes.py` ao `app/main.py`.
- [ ] **SQLModel Integration**: Migrar o armazenamento de memória para SQLite.
- [ ] **Injeção de Singleton**: Garantir que o repositório mantenha o estado entre requisições HTTP.
- [ ] **Filtros de Listagem**: Implementar `priority` e `status` como filtros no `GET /tasks`.

## 🧠 Milestone 2: AI Enhancements (v0.3.0)
- [ ] **Integração Real OpenAI**: Substituir stub por chamada real via LangChain.
- [ ] **Justificativa da IA**: Adicionar campo `priority_reason` ao modelo, explicando por que a IA escolheu aquela prioridade.
- [ ] **Análise em Lote**: Endpoint para re-priorizar todas as tarefas pendentes de uma vez.

## 🚀 Milestone 3: Production Ready (v1.0.0)
- [ ] Autenticação JWT.
- [ ] Dockerização (Dockerfile + Compose).
- [ ] CI/CD Pipeline (GitHub Actions para Pytest).

## 🛠️ Dívida Técnica e Qualidade (Próxima Sprint)
- [ ] **Fix Test Logs**: Corrigir propagação de log nos testes de fallback do `PriorityAdvisor`.
- [ ] **Schema Validation**: Adicionar testes para limites de caracteres no Pydantic.
- [ ] **Thread Safety**: Se mantiver in-memory, proteger o `_storage` com Lock/Semaphore.
- [ ] **API Error Handling**: Padronizar respostas de erro (404, 422, 500).
