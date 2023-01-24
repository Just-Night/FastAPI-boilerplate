#!/bin/sh

echo "Start migrate"

# autogenerete migrate
alembic revision --autogenerate
# make migrations
alembic upgrade head
