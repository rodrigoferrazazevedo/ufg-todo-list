# Documento de Escopo - MVP Task Manager AI

Este documento define os limites e requisitos do Produto Mínimo Viável (MVP) para a API de gestão de tarefas com priorização assistida por IA.

## 1. Objetivo
Desenvolver uma ferramenta de back-end que automatize a organização de tarefas através da análise de contexto via IA e heurísticas.

## 2. Requisitos Funcionais (RF)
- [x] **RF01 - CRUD de Tarefas:** Operações completas de criação, leitura, atualização e exclusão (Implementado).
- [x] **RF02 - Persistência Local (SQLite):** Implementado via SQLModel e base de dados física `database.db`.
- [x] **RF03 - Priorização Inteligente:** Integração automática no fluxo de criação de tarefas (Implementado via PriorityAdvisor).
- [ ] **RF04 - Filtro de Prioridade:** Adicionar parâmetros de query na listagem para filtrar por prioridade ou status (Pendente).
- [x] **RF05 - Verificação de Saúde:** Endpoint `/health` operacional (Implementado).

## 3. Requisitos Não Funcionais (RNF)
- [x] **RNF01 - Performance:** Uso extensivo de `async/await` e sessões de banco otimizadas.
- [x] **RNF02 - Segurança de Configuração:** Suporte a `.env` para chaves sensíveis.
- [x] **RNF03 - Documentação:** Swagger UI funcional em `/docs`.
- [x] **RNF04 - Tipagem:** Uso rigoroso de Type Hints, Pydantic V2 e SQLModel.

## 4. Próximas Implementações (Pós-MVP)
- Autenticação JWT e Multi-usuário.
- Sistema de Migrações de Banco de Dados (Alembic).
- Dashboard de métricas de produtividade.

## 5. Tecnologias Atuais
- **Linguagem:** Python 3.11+
- **Framework:** FastAPI
- **Banco de Dados:** SQLite + SQLModel
- **Testes:** Pytest (Cobertura de Rotas, Serviços e IA)
