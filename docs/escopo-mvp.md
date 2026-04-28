# Documento de Escopo - MVP Task Manager AI

Este documento define os limites e requisitos do Produto Mínimo Viável (MVP) para a API de gestão de tarefas com priorização assistida por IA.

## 1. Objetivo
Desenvolver uma ferramenta de back-end para equipes internas que automatize a organização de fluxos de trabalho através da análise de contexto das tarefas via LLM.

## 2. Requisitos Funcionais (RF)
- **RF01 - CRUD de Tarefas:** Criação, leitura, atualização e exclusão de tarefas.
- **RF02 - Persistência Local:** Armazenamento em banco de dados SQLite para fácil portabilidade.
- **RF03 - Priorização Inteligente:** Endpoint dedicado que envia a descrição da tarefa para uma IA e retorna uma sugestão de prioridade (High, Medium, Low) com justificativa.
- **RF04 - Filtro de Prioridade:** Listagem de tarefas filtradas por nível de prioridade ou status de conclusão.
- **RF05 - Verificação de Saúde:** Endpoint `/health` para monitoramento do status da aplicação.

## 3. Requisitos Não Funcionais (RNF)
- **RNF01 - Performance:** O processamento da IA não deve bloquear o loop principal da API (uso de `async/await`).
- **RNF02 - Segurança de Configuração:** Uso de variáveis de ambiente (`.env`) para chaves de API.
- **RNF03 - Documentação:** Disponibilidade imediata de Swagger UI (`/docs`).
- **RNF04 - Tipagem:** Cobertura total de tipos via Pydantic e Type Hints do Python.

## 4. Fora de Escopo
- Interface Gráfica (Frontend/Mobile).
- Autenticação e Autorização (nesta fase inicial).
- Suporte a múltiplos bancos de dados (PostgreSQL, etc.).
- Histórico de alterações de tarefas (Auditoria).

## 5. Tecnologias
- **Linguagem:** Python 3.11
- **Framework:** FastAPI
- **IA:** OpenAI API / LangChain
- **ORM:** SQLModel
