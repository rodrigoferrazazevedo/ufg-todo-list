# Backlog - Task Manager AI

## ✅ Concluído (v0.2.0)
- [x] Setup inicial e Health Check.
- [x] CRUD completo de tarefas (Routes, Service, Repository).
- [x] Lógica de IA híbrida (PriorityAdvisor) com Fallback Local.
- [x] Cobertura de testes automatizados (Pytest).
- [x] **Persistência SQLite com SQLModel**.
- [x] **Registro Global de Rotas no main.py**.
- [x] **Configuração de Sessões de Banco de Dados**.

## 🏁 Milestone 1: Enhancements & UI Readiness (v0.3.0)
- [ ] **Filtros de Listagem**: Implementar filtros por `status` e `priority` no `GET /tasks`.
- [ ] **Middleware de Erros**: Padronizar respostas de erro JSON globais.
- [ ] **Documentação de Schemas**: Adicionar descrições detalhadas e exemplos nos modelos do Swagger.

## 🧠 Milestone 2: AI Enhancements (v0.4.0)
- [ ] **Integração Real OpenAI**: Substituir stub por chamada real via LangChain.
- [ ] **Justificativa da IA**: Adicionar campo `priority_reason` ao modelo.
- [ ] **Análise em Lote**: Re-priorização de tarefas pendentes em massa.

## 🚀 Milestone 3: Production Ready (v1.0.0)
- [ ] Autenticação JWT.
- [ ] Sistema de Migrações (Alembic).
- [ ] Dockerização e CI/CD.

## 🛠️ Dívida Técnica e Qualidade
- [ ] **Fix Test Logs**: Corrigir propagação de log nos testes de fallback.
- [ ] **Schema Validation Tests**: Testar limites de caracteres e padrões regex.
- [ ] **Database Indexes**: Adicionar índices em campos de busca frequente.
