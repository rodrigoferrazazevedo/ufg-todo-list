from datetime import datetime
from fastapi import FastAPI

app = FastAPI(title="Task Manager AI")

@app.get("/health")
async def health_check() -> dict[str, str]:
    """
    Retorna o status atual da API e o timestamp do servidor.
    """
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat()
    }
