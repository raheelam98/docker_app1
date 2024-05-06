from docker_con1 import settings
from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Session

# create database schema
class Todo(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    todo_name : str
    #is_complete : bool = False

# connecting with database 
connection_string = str(settings.DATABASE_URL).replace("postgresql", "postgresql+psycopg2")

# create engine
engine = create_engine(connection_string, connect_args={"sslmode":"require"}, pool_recycle=300, echo=True)

# create database and tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# create session to get memory space in db
def get_session():
    with Session(engine) as session:
        yield session