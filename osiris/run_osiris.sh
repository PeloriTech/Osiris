#!/usr/bin/env bash
venv/bin/gunicorn osiris_server.wsgi -b :9000 --workers=5
