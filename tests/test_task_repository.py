import pytest
from uuid import uuid4
from sqlmodel import Session, SQLModel, create_engine
from sqlalchemy.pool import StaticPool
from app.repositories.task_repository import TaskRepository
from app.models.task import TaskCreate, TaskUpdate

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

@pytest.mark.asyncio
async def test_repository_save_and_find(session):
    repo = TaskRepository(session)
    task_data = TaskCreate(title="Repo Task", description="Testing Repo")
    
    # Test Save
    saved_task = await repo.save(task_data)
    assert saved_task.title == "Repo Task"
    assert saved_task.id is not None
    
    # Test Find by ID
    found_task = await repo.find_by_id(saved_task.id)
    assert found_task.id == saved_task.id
    assert found_task.title == "Repo Task"

@pytest.mark.asyncio
async def test_repository_find_all_with_filter(session):
    repo = TaskRepository(session)
    await repo.save(TaskCreate(title="Task 1", status="pending"))
    await repo.save(TaskCreate(title="Task 2", status="completed"))
    
    # Test find_all without filter
    all_tasks = await repo.find_all()
    assert len(all_tasks) == 2
    
    # Test find_all with filter
    completed_tasks = await repo.find_all(status="completed")
    assert len(completed_tasks) == 1
    assert completed_tasks[0].title == "Task 2"

@pytest.mark.asyncio
async def test_repository_update(session):
    repo = TaskRepository(session)
    task = await repo.save(TaskCreate(title="Old Title"))
    
    update_data = TaskUpdate(title="New Title", status="in_progress")
    updated_task = await repo.update(task.id, update_data)
    
    assert updated_task.title == "New Title"
    assert updated_task.status == "in_progress"

@pytest.mark.asyncio
async def test_repository_delete(session):
    repo = TaskRepository(session)
    task = await repo.save(TaskCreate(title="To Delete"))
    
    success = await repo.delete(task.id)
    assert success is True
    
    found = await repo.find_by_id(task.id)
    assert found is None
