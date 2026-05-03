# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/spec/v2.0.0.html).

## [0.2.1] - 2026-05-02

### Adicionado
- Dependências de teste (`pytest-asyncio`, `httpx`) incluídas explicitamente no `requirements.txt`.

### Modificado
- Versões das dependências fixadas no `requirements.txt` para garantir estabilidade (FastAPI, SQLModel).
- Atualizadas docstrings dos endpoints para melhor clareza no Swagger UI.
- Migrado uso de `datetime.utcnow()` para `datetime.now(timezone.utc)` nos testes (removendo avisos de depreciação).

## [0.2.0] - 2026-05-02

### Adicionado
- Persistência real utilizando **SQLite** e **SQLModel**.
- Registro global de rotas no arquivo principal `main.py`.
- Configuração de sessões de banco de dados via injeção de dependência.
- Inicialização automática de tabelas no startup da API.
- Relato detalhado de assistência de IA em `docs/relatorio-ia.md`.

### Modificado
- `TaskRepository` convertido de armazenamento em memória para persistência em banco de dados.
- `README.md` atualizado com links de navegação e checklist técnico revisado.

## [0.1.0] - 2026-05-02

### Adicionado
- Estrutura base da API com FastAPI.
- Implementação da camada de serviço (`TaskService`) e repositório (`TaskRepository`).
- Componente `PriorityAdvisor` com lógica híbrida de IA e heurística local.
- Suíte de testes automatizados com `pytest` (Rotas, Serviços e IA).
- Documentação inicial de Arquitetura, Escopo e Backlog na pasta `docs/`.

---
*Nota: Este projeto foi desenvolvido com suporte de IA (Gemini CLI).*
