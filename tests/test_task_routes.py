import pytest
from fastapi.testclient import TestClient
from uuid import uuid4
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock

from app.main import app
from app.api.task_routes import router, get_task_service
from app.models.task import TaskOut

# Incluímos o roteador no app para o teste, caso ele ainda não esteja lá
app.include_router(router)

client = TestClient(app)

@pytest.fixture
def mock_service():
    """Cria um mock para o TaskService."""
    return AsyncMock()

@pytest.fixture
def override_dependencies(mock_service):
    """Injeta o mock_service como dependência nos endpoints."""
    app.dependency_overrides[get_task_service] = lambda: mock_service
    yield
    app.dependency_overrides.clear()

@pytest.fixture
def sample_task_out():
    now = datetime.now(timezone.utc)
    return {
        "id": str(uuid4()),
        "title": "Test Task",
        "description": "Test Description",
        "status": "pending",
        "created_at": now.isoformat(),
        "updated_at": now.isoformat()
    }

def test_create_task_success(override_dependencies, mock_service, sample_task_out):
    """Testa a criação de uma tarefa (POST /tasks/) -> 201."""
    # Arrange
    mock_service.create_task.return_value = TaskOut(**sample_task_out)
    payload = {"title": "New Task", "description": "New Description"}

    # Act
    response = client.post("/tasks/", json=payload)

    # Assert
    assert response.status_code == 201
    assert response.json()["title"] == "Test Task"
    mock_service.create_task.assert_called_once()

def test_list_tasks_success(override_dependencies, mock_service, sample_task_out):
    """Testa a listagem de tarefas (GET /tasks/) -> 200."""
    # Arrange
    mock_service.get_all_tasks.return_value = [TaskOut(**sample_task_out)]

    # Act
    response = client.get("/tasks/")

    # Assert
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["id"] == sample_task_out["id"]

def test_get_task_by_id_not_found(override_dependencies, mock_service):
    """Testa a busca de uma tarefa inexistente (GET /tasks/{id}) -> 404."""
    # Arrange
    mock_service.get_task_by_id.return_value = None
    task_id = uuid4()

    # Act
    response = client.get(f"/tasks/{task_id}")

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]

def test_update_task_success(override_dependencies, mock_service, sample_task_out):
    """Testa a atualização de uma tarefa (PUT /tasks/{id}) -> 200."""
    # Arrange
    mock_service.update_task.return_value = TaskOut(**sample_task_out)
    task_id = sample_task_out["id"]
    payload = {"title": "Updated Title"}

    # Act
    response = client.put(f"/tasks/{task_id}", json=payload)

    # Assert
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"

def test_delete_task_success(override_dependencies, mock_service):
    """Testa a remoção de uma tarefa (DELETE /tasks/{id}) -> 204."""
    # Arrange
    mock_service.delete_task.return_value = True
    task_id = uuid4()

    # Act
    response = client.delete(f"/tasks/{task_id}")

    # Assert
    assert response.status_code == 204
    assert response.content == b""

def test_delete_task_not_found(override_dependencies, mock_service):
    """Testa a remoção de uma tarefa inexistente (DELETE /tasks/{id}) -> 404."""
    # Arrange
    mock_service.delete_task.return_value = False
    task_id = uuid4()

    # Act
    response = client.delete(f"/tasks/{task_id}")

    # Assert
    assert response.status_code == 404
