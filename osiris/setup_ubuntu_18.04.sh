#!/usr/bin/env bash

# Web
export SQL_DATABASE=osiris_db
export SQL_HOST=localhost
export SQL_PORT=5432
export SQL_USER=osiris_user
export SQL_ENGINE=django.db.backends.postgresql
export DATABASE=postgres

#postgres/python
sudo apt update
sudo apt install -y python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl virtualenv python3.6


# create db
#setup database
sudo -u postgres createdb osiris_db

sudo -u postgres createuser osiris_user
sudo -u postgres createdb osiris_db
sudo -u postgres psql -c "ALTER USER osiris_user with password 'osiris_password'"
sudo -u postgres psql -c "ALTER USER osiris_user with SUPERUSER"
sudo -u postgres psql -d "osiris_db" -c "GRANT ALL PRIVILEGES on DATABASE osiris_db to osiris_user;"

#DB
export POSTGRES_DB=osiris_db
export POSTGRES_PASSWORD=osiris_passwordi

#virtualenv

pip3 install --upgrade pip
virtualenv --system-site-packages venv --python=python3.6
venv/bin/pip install -r requirements.txt


# install opencv

sudo sh scripts/install-opencv-2.sh

#venv/bin/python3.6 manage.py makemigrations osiris_server
venv/bin/python3.6 manage.py migrate
