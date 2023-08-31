#!/bin/bash

echo "Waiting for progres ..."

while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
    sleep 0.1
    done

    echo "PostgresSQL started"

exec "$@"
