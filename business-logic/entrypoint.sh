#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations survey
python manage.py migrate
echo "MIGRATED"
# python manage.py createsuperuser --username admin --email admin@email.com
python preload_database.py
exec "$@"
