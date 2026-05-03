from datetime import datetime, timezone
from fastapi import FastAPI
from app.api.task_routes import router as task_router
from app.database import create_db_and_tables

app = FastAPI(title="Task Manager AI")

# Cria as tabelas no banco de dados SQLite no startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Registro de rotas
app.include_router(task_router)

@app.get("/health")
async def health_check() -> dict[str, str]:
    """
    Retorna o status atual da API e o timestamp do servidor.
    """
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
