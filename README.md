# Task Manager AI

API minimalista para gestão de tarefas com priorização inteligente assistida por IA.

## 🎯 Objetivo
Prover uma interface eficiente para criação e organização de tarefas, utilizando modelos de linguagem (LLMs) para analisar a urgência e importância de cada item, automatizando a definição de prioridades e otimizando o fluxo de trabalho.

## 🛠 Stack Técnica
- **Linguagem:** Python 3.10+
- **Framework:** FastAPI
- **Banco de Dados:** SQLite (SQLModel/SQLAlchemy)
- **IA:** OpenAI API / LangChain
- **Validação:** Pydantic

## 🚀 Como Rodar Localmente

1. **Ative o ambiente virtual:**
   ```bash
   source .env/bin/activate
   ```

2. **Instale as dependências:**
   *(Arquivo requirements.txt será gerado em breve)*
   ```bash
   pip install fastapi uvicorn sqlmodel
   ```

3. **Inicie a aplicação:**
   ```bash
   uvicorn main:app --reload
   ```
   Acesse a documentação interativa em: `http://127.0.0.1:8000/docs`

## 🗺 Roadmap de Releases

### v0.1.0 - MVP Foundation
- CRUD básico de tarefas (Título, Descrição, Status).
- Persistência em banco de dados local (SQLite).
- Estrutura base da API e documentação automática.

### v0.2.0 - IA Integration
- Integração com LLM para análise de contexto de tarefas.
- Sugestão automática de prioridade (Alta, Média, Baixa) baseada na descrição.
- Endpoint de "Smart Sort" para ordenar lista por impacto.

### v1.0.0 - Production Ready
- Sistema de autenticação (JWT).
- Suporte a múltiplos usuários/projetos.
- Dockerização e guia de deploy.

---
*Projeto em desenvolvimento para o laboratório de software.*
