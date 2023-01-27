import typer
import subprocess
import os

app = typer.Typer()

model_text = """from database import BASE_MODEL
from sqlalchemy import(  # noqa: disable=F401
    Table,
    Column,
    ForeignKey,
    String,
    Text,
    text,
    Integer,
    BIGINT,
    Boolean,
    DateTime,
    TIMESTAMP,
    ARRAY
    )
"""
schemas_text = """from typing import List, Optional  # noqa: disable=F401
from uuid import UUID
from pydantic import BaseModel


class Base(BaseModel):
    id: Optional[UUID]

    class Config:
        orm_mode = True
"""
views_text = """from fastapi import APIRouter


router = APIRouter(
    prefix='/default_app',
    tags=["default app"]
)
"""


def folder_create(path):
    os.mkdir(f'./apps/{path}')


def folder_check(path):
    if os.path.exists(path):
        raise print("Folder exists")


def file_create(path: str, file_name: str):
    return open(os.path.join(f'./apps/{path}', file_name), 'w')


def file_write(file, text: str):
    file.write(text)
    file.close()


def create_default_app(path: str):
    file_create(path, '__init__.py')
    file_write(file_create(path, 'model.py'), model_text)
    file_write(file_create(path, 'schemas.py'), schemas_text)
    file_write(file_create(path, 'views.py'), views_text)


@app.command()
def check():
    subprocess.run(['bash', './scripts/check.sh'])


@app.command()
def migrate():
    subprocess.run(['bash', './scripts/migrate.sh'])


@app.command()
def generate_key(number: str = 32):
    subprocess.run(['bash', './scripts/generate_key.sh', number])


@app.command()
def create_app(path: str):
    folder_check(path)
    folder_create(path)
    create_default_app(path)


if __name__ == "__main__":
    app()
