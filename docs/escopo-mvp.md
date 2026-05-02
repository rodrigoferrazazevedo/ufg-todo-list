# Documento de Escopo - MVP Task Manager AI

Este documento define os limites e requisitos do Produto Mínimo Viável (MVP) para a API de gestão de tarefas com priorização assistida por IA.

## 1. Objetivo
Desenvolver uma ferramenta de back-end que automatize a organização de tarefas através da análise de contexto via IA e heurísticas.

## 2. Requisitos Funcionais (RF)
- [x] **RF01 - CRUD de Tarefas:** Operações completas de criação, leitura, atualização e exclusão (Implementado).
- [ ] **RF02 - Persistência Local (SQLite):** Atualmente utiliza armazenamento em memória. Migração para SQLite agendada para v0.2.0.
- [x] **RF03 - Priorização Inteligente:** Integração automática no fluxo de criação de tarefas (Implementado via PriorityAdvisor).
- [ ] **RF04 - Filtro de Prioridade:** Adicionar parâmetros de query na listagem para filtrar por prioridade ou status (Pendente).
- [x] **RF05 - Verificação de Saúde:** Endpoint `/health` operacional (Implementado).

## 3. Requisitos Não Funcionais (RNF)
- [x] **RNF01 - Performance:** Uso extensivo de `async/await` para evitar bloqueios no processamento da IA.
- [x] **RNF02 - Segurança de Configuração:** Suporte a `.env` para chaves sensíveis.
- [x] **RNF03 - Documentação:** Swagger UI funcional em `/docs`.
- [x] **RNF04 - Tipagem:** Uso rigoroso de Type Hints e Pydantic V2.

## 4. Próximas Implementações (Pós-MVP)
- Autenticação JWT e Multi-usuário.
- Persistência persistente via SQLModel.
- Dashboard de métricas de produtividade.

## 5. Tecnologias Atuais
- **Linguagem:** Python 3.11+
- **Framework:** FastAPI
- **Testes:** Pytest (Cobertura de Rotas, Serviços e IA)
- **Modelagem:** Pydantic V2
