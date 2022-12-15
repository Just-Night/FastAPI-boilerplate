#!/bin/sh
echo "Start migrate"
# autogenerete migrate
alembic -c ./migrations/alembic.ini revision --autogenerate
# make migrations
alembic -c ./migrations/alembic.ini  upgrade head
