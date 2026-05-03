from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.pool import StaticPool

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# O connect_args={"check_same_thread": False} é necessário apenas para o SQLite
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
