import pytest
import asyncio
from unittest.mock import AsyncMock, patch
from app.services.priority_advisor import PriorityAdvisor

@pytest.fixture
def advisor():
    return PriorityAdvisor()

@pytest.mark.asyncio
async def test_suggest_priority_high_by_heuristic(advisor):
    """Garante que palavras-chave críticas retornam prioridade 'high' via heurística."""
    # Arrange
    title = "Corrigir erro crítico no sistema"
    description = "O banco de dados está parado"
    
    # Act
    priority = await advisor.suggest_priority(title, description)
    
    # Assert
    assert priority == "high"

@pytest.mark.asyncio
async def test_suggest_priority_medium_by_heuristic(advisor):
    """Garante que palavras-chave de importância moderada retornam 'medium' via heurística."""
    # Arrange
    title = "Revisão de código pendente"
    description = "Melhoria na performance amanhã"
    
    # Act
    priority = await advisor.suggest_priority(title, description)
    
    # Assert
    assert priority == "medium"

@pytest.mark.asyncio
async def test_suggest_priority_low_by_default(advisor):
    """Garante que tarefas sem palavras-chave específicas retornam 'low' por padrão."""
    # Arrange
    title = "Comprar café"
    description = "Verificar marcas disponíveis"
    
    # Act
    priority = await advisor.suggest_priority(title, description)
    
    # Assert
    assert priority == "low"

@pytest.mark.asyncio
async def test_suggest_priority_fallback_on_llm_failure(advisor, monkeypatch):
    """Garante que a heurística local é usada se o LLM falhar (fallback)."""
    # Arrange
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")
    # Força erro na chamada simulada do LLM
    with patch.object(PriorityAdvisor, "_ask_llm", side_effect=Exception("API Error")):
        title = "Urgente: Erro na API"
        
        # Act
        priority = await advisor.suggest_priority(title)
        
        # Assert
        assert priority == "high"  # Usou a heurística local

@pytest.mark.asyncio
async def test_suggest_priority_fallback_on_llm_timeout(advisor, monkeypatch):
    """Garante fallback para heurística local em caso de timeout na resposta do LLM."""
    # Arrange
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")
    
    async def slow_response(*args, **kwargs):
        await asyncio.sleep(1.0)
        return "high"

    # Reduz timeout para o teste ser rápido
    advisor.timeout = 0.1
    
    with patch.object(PriorityAdvisor, "_ask_llm", side_effect=slow_response):
        title = "Tarefa importante"
        
        # Act
        priority = await advisor.suggest_priority(title)
        
        # Assert
        assert priority == "medium"  # 'importante' -> medium via heurística

