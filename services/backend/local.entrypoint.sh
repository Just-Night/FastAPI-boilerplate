#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# python manage.py migrate --no-input
# python manage.py collectstatic --no-input

uvicorn main:app --host 0.0.0.0 --port 8000 --reload
