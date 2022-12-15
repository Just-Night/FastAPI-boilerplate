#!/usr/bin/env python
import os
import subprocess


def main():
    """Run administrative tasks."""
    print("select\n1 - create SuperUser\n2 - migrate\n0 - exit")
    parametr = int(input())
    if parametr == 1:
        # login = str(input("login: "))
        # password = str(input("password: "))
        print("SuperUser create")
    elif parametr == 2:
        subprocess.Popen('alembic -c ./migrations/alembic.ini revision --autogenerate')
    else:
        print("exit")


if __name__ == '__main__':
    main()
