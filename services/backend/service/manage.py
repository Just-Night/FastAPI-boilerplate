import typer
import subprocess
import os
import getpass
from database import db_session
from apps.auth.schemas import OAuth2
from crud import UserCRUD


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
    if os.path.exists(f"./apps/{path}"):
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


def check_password(first: str, last: str):
    if last != first:
        return False


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


@app.command()
def create_syperuser(login=None, password=None, pass_again=None):
    if login or password or pass_again is None:
        login = input('Input login: ')
        password = getpass.getpass('Input password: ')
        pass_again = getpass.getpass('Input password again: ')
    if check_password(password, pass_again) is False:
        return print("password incorrect")
    user = UserCRUD.create_superuser(db_session, obj_in=OAuth2(login=login, password=password))
    if user is True:
        print("Successful create!")
    else:
        print('User login already exists')


if __name__ == "__main__":
    app()
