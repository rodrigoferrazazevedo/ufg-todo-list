# Task Manager AI - Micro-API de Gerenciamento de Tarefas

[![Changelog](https://img.shields.io/badge/changelog-v0.3.0-blue)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

API RESTful para gerenciamento de tarefas (To-Do List) com diferencial de **Priorização Assistida por Inteligência Artificial**. O sistema analisa semânticamente o título e a descrição das tarefas para sugerir automaticamente sua urgência.

## 🚀 O que é o MVP? (Descrição)
Este MVP é uma ferramenta de produtividade voltada para automação de triagem de tarefas. Ao criar uma tarefa, o usuário não precisa se preocupar em definir a prioridade manualmente; o sistema utiliza uma abordagem híbrida (IA + Heurística) para classificar a tarefa entre `high`, `medium` ou `low`.

---

## 🛠️ Arquitetura e Decisões Técnicas

O projeto foi construído seguindo princípios de **Engenharia de Software Moderna**, garantindo que o sistema seja **reproduzível, auditável e evoluível**.

### 1. Padrões de Projeto (Justificativas)
- **SOLID (SRP & DIP):**
    - **Single Responsibility Principle (SRP):** Cada camada tem uma responsabilidade única. As rotas apenas gerenciam HTTP, o serviço orquestra a lógica e o repositório lida exclusivamente com o banco de dados.
    - **Dependency Inversion Principle (DIP):** O uso de Injeção de Dependência do FastAPI facilita o teste e a troca de componentes (ex: trocar SQLite por PostgreSQL sem alterar a lógica).
- **Repository Pattern:** Abstrai a persistência, permitindo que a lógica de negócio ignore detalhes de implementação do banco de dados.
- **Service Layer:** Centraliza as regras de negócio, facilitando a reutilização e garantindo que os endpoints da API permaneçam enxutos.

### 2. Escolha da Stack
- **FastAPI:** Escolhido pela alta performance (async/await), tipagem forte e documentação automática (OpenAPI).
- **SQLModel (SQLAlchemy + Pydantic):** Unifica a definição de modelos de dados e schemas de validação, reduzindo duplicação de código (DRY).
- **SQLite:** Adotado pela simplicidade e portabilidade, sendo ideal para um MVP e facilitando a avaliação direta sem setup complexo de infraestrutura.

---

## 🏃 Como Rodar o Projeto

### Pré-requisitos
- Python 3.9+
- Makefile (opcional, mas recomendado)

### Execução Automática (Makefile)
```bash
make install  # Instala dependências
make test     # Executa todos os testes (Pytest)
make run      # Inicia o servidor local em http://127.0.0.1:8000
```

### Execução Manual
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🔌 Exemplos de Interação (curl)

### 1. Criar uma Tarefa (Com priorização automática)
```bash
curl -X POST "http://127.0.0.1:8000/tasks/" \
     -H "Content-Type: application/json" \
     -d '{"title": "Corrigir erro crítico", "description": "O sistema está parado"}'
```

### 2. Listar Tarefas (Filtrar por Status)
```bash
curl -X GET "http://127.0.0.1:8000/tasks/?status=pending"
```

### 3. Atualizar Tarefa (Marcar como concluída)
```bash
curl -X PUT "http://127.0.0.1:8000/tasks/<ID-DO-UUID>" \
     -H "Content-Type: application/json" \
     -d '{"status": "completed"}'
```

---

## 🧠 Assistência de IA

Este projeto utilizou a **IA Gemini CLI** como um **Pair Programmer Sênior**.

### Como a IA foi utilizada:
- **QA Automatizado:** Geração ágil de 24 testes cobrindo rotas, repositórios e serviços.
- **Refatoração:** Apoio na transição de In-Memory para SQLite mantendo os princípios SOLID.
- **Documentação:** Auxílio na manutenção do Changelog e Relato de IA.

### Limitações da IA:
- A IA pode sugerir padrões genéricos se não for guiada pelo contexto local.
- Depende de validação humana para integração com credenciais reais (OpenAI keys).

---

## ⚠️ Limitações e Próximos Passos

### Limitações Atuais:
- **Autenticação:** Não há controle de usuários nesta versão.
- **Concorrência:** Uso de SQLite em modo simples (não ideal para alta escala).
- **IA Real:** O PriorityAdvisor opera em modo stub por padrão para evitar custos de API sem autorização do usuário.

### Evolução Planejada:
- [ ] Implementação de **JWT Authentication**.
- [ ] Integração real com **OpenAI/LangChain** configurável via `.env`.
- [ ] Migração para **PostgreSQL** via Docker Compose para produção.
