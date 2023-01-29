# FastAPI-boilerplate

## manage.py command
   - check - checks the database for upgrades
   - migrate - migrate database
   - generate-key  number (default 32) - generate a random key
   - create-app name - creates app with default files
   - create-syperuser - create syper user

## env example

   - ### api:
        ```
        # database
        DATABASE=postgres
        POSTGRES_DB=postgres
        POSTGRES_USER=postgres
        POSTGRES_PASSWORD=postgres
        DB_HOST=pgdb
        DB_PORT=5432

        # FastAPI
        PROJECT_NAME=
        DEBUG=1
        ASYNC=0
        SECRET_KEY=
        DOCKS_URL=/docs
        REDOC_URL=
        ALLOWED_HOSTS=0.0.0.0,localhost
        CORS_ALLOW_METHODS=GET,POST,PUT,PATCH,DELETE,OPTIONS
        CORS_ALLOWED_ORIGINS=http://0.0.0.0,http://localhost,http://localhost:8000
        CSRF_TRUSTED_ORIGINS=http://0.0.0.0,http://localhost,http://localhost:8000
        ```
   - ### postgres:
        ```
        # database
        DATABASE=postgres
        POSTGRES_DB=postgres
        POSTGRES_USER=postgres
        POSTGRES_PASSWORD=postgres
        DB_HOST=pgdb
        DB_PORT=5432
        ```
