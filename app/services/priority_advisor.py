import os
import asyncio
import logging
from typing import Optional

# Configuração básica de logging
logger = logging.getLogger(__name__)

class PriorityAdvisor:
    """
    Componente especializado em sugerir prioridades para tarefas.
    Utiliza uma abordagem híbrida: LLM (OpenAI) se disponível, 
    ou Heurística Local como fallback seguro.
    """

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.timeout = 5.0  # Timeout rigoroso de 5 segundos

    async def suggest_priority(self, title: str, description: Optional[str] = None) -> str:
        """
        Tenta obter sugestão via LLM, caso contrário usa heurística local.
        """
        if self.api_key:
            try:
                # Chamada protegida por timeout
                return await asyncio.wait_for(self._ask_llm(title, description), timeout=self.timeout)
            except Exception as e:
                logger.error(f"Falha na chamada ao LLM: {e}. Acionando fallback local.")
        
        return self._local_heuristic(title, description)

    async def _ask_llm(self, title: str, description: str) -> str:
        """
        Simula/Realiza a chamada para a API da OpenAI.
        """
        # Aqui entraria a integração real via langchain ou openai client
        # Por enquanto, simulamos uma latência de rede
        await asyncio.sleep(0.5)
        
        # Lógica simplificada de retorno do modelo
        return "high" # Exemplo de retorno da IA

    def _local_heuristic(self, title: str, description: str) -> str:
        """
        Heurística local baseada em palavras-chave (sem custo de API).
        """
        text = f"{title} {description or ''}".lower()
        
        high_priority_terms = ["urgente", "imediato", "erro", "bug", "crítico", "parado"]
        medium_priority_terms = ["importante", "melhoria", "amanhã", "revisão"]

        if any(term in text for term in high_priority_terms):
            return "high"
        if any(term in text for term in medium_priority_terms):
            return "medium"
        
        return "low"
