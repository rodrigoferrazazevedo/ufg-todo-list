# Backlog - Task Manager AI

Lista de tarefas prioritárias organizadas por marcos de entrega.

## 🏁 Milestone 1: MVP Foundation (v0.1.0)
- [x] Configuração inicial do repositório (.gitignore, venv, requirements).
- [x] Definição de README e Escopo.
- [x] Endpoint de `/health`.
- [ ] Modelagem do banco de dados com SQLModel (Tarefa: id, title, description, priority, status).
- [ ] Configuração da conexão com SQLite e migrações.
- [ ] Implementação do CRUD de tarefas:
    - [ ] `POST /tasks`: Criar nova tarefa.
    - [ ] `GET /tasks`: Listar todas as tarefas.
    - [ ] `GET /tasks/{id}`: Obter detalhe de uma tarefa.
    - [ ] `PATCH /tasks/{id}`: Atualizar tarefa.
    - [ ] `DELETE /tasks/{id}`: Remover tarefa.

## 🧠 Milestone 2: AI Integration (v0.2.0)
- [ ] Configuração da estrutura de serviços para IA.
- [ ] Implementação de Service para integração com OpenAI/LangChain.
- [ ] Endpoint `POST /tasks/{id}/prioritize`:
    - Envia descrição para IA e atualiza o campo `priority` automaticamente.
- [ ] Endpoint `GET /tasks/smart-sort`:
    - Retorna lista ordenada por sugestão da IA.

## 🚀 Milestone 3: Production Ready (v1.0.0)
- [ ] Implementação de Autenticação JWT.
- [ ] Adição de campo `owner_id` nas tarefas.
- [ ] Criação de Dockerfile e docker-compose.yml.
- [ ] Configuração de testes automatizados com Pytest.

## 📝 Documentação e Melhorias
- [ ] Adição de docstrings em todos os endpoints.
- [ ] Configuração de logs da aplicação.
- [ ] Tratamento global de exceções.

## 🛠️ Dívida Técnica e Qualidade
- [ ] **Refatorar Injeção de Dependência**: Substituir a instanciação manual no router por um sistema de DI (ex: `FastAPI Depends`) para facilitar mocks.
- [ ] **Desacoplar IO do Advisor**: Isolar a leitura de variáveis de ambiente e logs para tornar o componente mais testável.
- [ ] **Validar Entradas no Advisor**: Adicionar verificações para títulos vazios ou apenas com espaços.
- [ ] **Robustez no Repositório**: Implementar tratamento de exceções de banco de dados e validações de integridade.

## 🧪 Testes Prioritários (Próxima Release)
- [ ] **Teste de Fallback**: Validar heurística local quando o LLM falha ou está sem chave.
- [ ] **Teste de Integração de Serviço**: Validar `TaskService` com repositório mockado.
- [ ] **Teste de Erros HTTP**: Validar retornos 404 para recursos inexistentes.
- [ ] **Teste de Schema**: Validar restrições de caracteres e campos obrigatórios via Pydantic.
- [ ] **Teste de Idempotência**: Validar comportamento de exclusão repetida.
