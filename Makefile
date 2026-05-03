# Variáveis
PYTHON = python3
PIP = pip
UVICORN = uvicorn
PYTEST = pytest
APP_MODULE = app.main:app

.PHONY: help install run test clean

help: ## Exibe esta ajuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Instala as dependências do projeto
	$(PIP) install -r requirements.txt

run: ## Executa a API localmente via uvicorn
	$(UVICORN) $(APP_MODULE) --reload

test: ## Executa a suíte de testes com pytest
	$(PYTEST) tests/

clean: ## Remove arquivos temporários e cache do Python
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -exec rm -f {} +
	rm -rf .pytest_cache
	rm -f database.db
