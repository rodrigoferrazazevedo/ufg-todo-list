import pytest
from uuid import uuid4
from unittest.mock import AsyncMock, MagicMock
from datetime import datetime, timezone
from app.services.task_service import TaskService
from app.models.task import TaskCreate, TaskUpdate, TaskOut

@pytest.fixture
def mock_repository():
    return AsyncMock()

@pytest.fixture
def mock_priority_advisor():
    advisor = AsyncMock()
    advisor.suggest_priority.return_value = "medium"
    return advisor

@pytest.fixture
def task_service(mock_repository, mock_priority_advisor):
    return TaskService(repository=mock_repository, priority_advisor=mock_priority_advisor)

@pytest.fixture
def sample_task_out():
    now = datetime.now(timezone.utc)
    return TaskOut(
        id=uuid4(),
        title="Test Task",
        description="Test Description",
        status="pending",
        created_at=now,
        updated_at=now
    )

@pytest.mark.asyncio
async def test_create_task_should_return_task_with_priority_suggestion(
    task_service, mock_repository, mock_priority_advisor, sample_task_out
):
    # Arrange
    task_data = TaskCreate(title="New Task", description="Some description")
    mock_repository.save.return_value = sample_task_out
    
    # Act
    result = await task_service.create_task(task_data)
    
    # Assert
    assert result == sample_task_out
    mock_priority_advisor.suggest_priority.assert_called_once_with(
        title=task_data.title, 
        description=task_data.description
    )
    mock_repository.save.assert_called_once_with(task_data, priority_hint="medium")

@pytest.mark.asyncio
async def test_get_all_tasks_should_return_list(task_service, mock_repository, sample_task_out):
    # Arrange
    mock_repository.find_all.return_value = [sample_task_out]
    
    # Act
    result = await task_service.get_all_tasks()
    
    # Assert
    assert len(result) == 1
    assert result[0] == sample_task_out
    mock_repository.find_all.assert_called_once()

@pytest.mark.asyncio
async def test_get_task_by_id_should_return_task_when_exists(task_service, mock_repository, sample_task_out):
    # Arrange
    task_id = sample_task_out.id
    mock_repository.find_by_id.return_value = sample_task_out
    
    # Act
    result = await task_service.get_task_by_id(task_id)
    
    # Assert
    assert result == sample_task_out
    mock_repository.find_by_id.assert_called_once_with(task_id)

@pytest.mark.asyncio
async def test_get_task_by_id_should_return_none_when_not_found(task_service, mock_repository):
    # Arrange
    task_id = uuid4()
    mock_repository.find_by_id.return_value = None
    
    # Act
    result = await task_service.get_task_by_id(task_id)
    
    # Assert
    assert result is None
    mock_repository.find_by_id.assert_called_once_with(task_id)

@pytest.mark.asyncio
async def test_update_task_should_return_updated_task_when_exists(task_service, mock_repository, sample_task_out):
    # Arrange
    task_id = sample_task_out.id
    update_data = TaskUpdate(title="Updated Title")
    mock_repository.update.return_value = sample_task_out
    
    # Act
    result = await task_service.update_task(task_id, update_data)
    
    # Assert
    assert result == sample_task_out
    mock_repository.update.assert_called_once_with(task_id, update_data)

@pytest.mark.asyncio
async def test_update_task_should_return_none_when_not_found(task_service, mock_repository):
    # Arrange
    task_id = uuid4()
    update_data = TaskUpdate(title="Updated Title")
    mock_repository.update.return_value = None
    
    # Act
    result = await task_service.update_task(task_id, update_data)
    
    # Assert
    assert result is None
    mock_repository.update.assert_called_once_with(task_id, update_data)

@pytest.mark.asyncio
async def test_delete_task_should_return_true_on_success(task_service, mock_repository):
    # Arrange
    task_id = uuid4()
    mock_repository.delete.return_value = True
    
    # Act
    result = await task_service.delete_task(task_id)
    
    # Assert
    assert result is True
    mock_repository.delete.assert_called_once_with(task_id)

@pytest.mark.asyncio
async def test_delete_task_should_return_false_when_fails(task_service, mock_repository):
    # Arrange
    task_id = uuid4()
    mock_repository.delete.return_value = False
    
    # Act
    result = await task_service.delete_task(task_id)
    
    # Assert
    assert result is False
    mock_repository.delete.assert_called_once_with(task_id)
