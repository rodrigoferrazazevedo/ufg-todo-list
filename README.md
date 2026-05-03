# Task Manager AI - Micro-API de Gerenciamento de Tarefas

[![Changelog](https://img.shields.io/badge/changelog-v0.3.0-blue)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

API RESTful para gerenciamento de tarefas (To-Do List) com diferencial de **Priorização Assistida por Inteligência Artificial**. O sistema analisa semânticamente o título e a descrição das tarefas para sugerir automaticamente sua urgência.

## 🚀 O que é o MVP? (Descrição)
Este MVP é uma ferramenta de produtividade voltada para automação de triagem de tarefas. Ao criar uma tarefa, o usuário não precisa se preocupar em definir a prioridade manualmente; o sistema utiliza uma abordagem híbrida (IA + Heurística) para classificar a tarefa entre `high`, `medium` ou `low`.

---

## 🛠️ Arquitetura e Decisões Técnicas

O projeto segue princípios de **Engenharia de Software Moderna**, garantindo que o sistema seja **reproduzível, auditável e evoluível**. Para uma visão detalhada, consulte nosso [Documento de Arquitetura](docs/arquitetura.md).

### 1. Padrões de Projeto (Justificativas)
- **SOLID (SRP & DIP):**
    - **Single Responsibility Principle (SRP):** Cada camada tem uma responsabilidade única. As rotas gerenciam HTTP, o serviço orquestra a lógica e o repositório lida com o banco de dados.
    - **Dependency Inversion Principle (DIP):** O uso de Injeção de Dependência do FastAPI facilita o teste e a troca de componentes.
- **Repository Pattern:** Abstrai a persistência, permitindo que a lógica de negócio ignore detalhes de implementação do banco de dados.
- **Service Layer:** Centraliza as regras de negócio, facilitando a reutilização e mantendo os endpoints enxutos.

### 2. Escolha da Stack
- **FastAPI:** Alta performance (async/await) e documentação automática.
- **SQLModel (SQLAlchemy + Pydantic):** Unifica modelos de dados e schemas de validação (DRY).
- **SQLite:** Portabilidade e simplicidade para um MVP.

---

## 🏃 Como Rodar o Projeto

### Pré-requisitos
- Python 3.9+
- Makefile (opcional, mas recomendado)

### Execução Rápida (Makefile)
```bash
make install  # Instala dependências
make test     # Executa a suíte de 24 testes (Pytest)
make run      # Inicia o servidor local em http://127.0.0.1:8000
make clean    # Limpa cache e arquivos temporários
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

## 🧠 Inteligência Artificial e Heurísticas

O sistema de prioridade opera em três níveis de confiança. Detalhes sobre o planejamento podem ser vistos no [Documento de Escopo](docs/escopo-mvp.md).

1. **LLM (OpenAI):** Tenta uma análise semântica profunda via API.
2. **Fallback (Timeout/Erro):** Se a API falhar ou demorar, o sistema aciona a heurística local.
3. **Heurística Local:** Analisa palavras-chave para determinar a prioridade sem custo ou latência.

---

## 🔍 Checklist Técnico e Evolução

### **Riscos Técnicos Restantes**
* **Concorrência:** SQLite deve ser monitorado em cenários de múltiplos acessos simultâneos de escrita.
* **Stub de IA:** A integração real com LangChain/OpenAI exige configuração de chaves reais no `.env`.

### **Melhorias Concluídas**
* ✅ **Persistência Real:** SQLite com SQLModel.
* ✅ **Filtro de Status:** Parâmetro `?status=` na listagem.
* ✅ **Licenciamento:** Licença MIT incluída.
* ✅ **QA Robusto:** 24 testes cobrindo todas as camadas.

O acompanhamento detalhado pode ser feito através do nosso [Backlog Completo](docs/backlog.md).

---

## 🤖 Assistência de IA

Este projeto foi desenvolvido com suporte da **Gemini CLI**, atuando como parceiro de programação sênior.

**Destaques da Colaboração:**
* **QA Automatizado:** Geração de 24 testes de unidade e integração.
* **Refatoração:** Transição segura para SQLite mantendo princípios SOLID.
* **Documentação:** Manutenção sincronizada de diagramas e análise de riscos.

Consulte o [Relato Completo de Assistência de IA](docs/relatorio-ia.md) para mais detalhes.
