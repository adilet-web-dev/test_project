#!/usr/bin/env bash

echo -e "Wait for database\n"
POSTGRES_TCP=$(echo "$DATABASE_URL" | sed 's/^postgres/tcp/')
dockerize -wait "$POSTGRES_TCP" -timeout 20s

if [[ "$1" = "test" ]]; then
    echo -e "Running tests\n"
    python manage.py test
else
    echo -e "Migrating database\n"
    python manage.py migrate

    echo -e "Starting server\n"
    gunicorn config.wsgi
fi
