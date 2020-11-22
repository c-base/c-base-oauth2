#!/bin/bash

POETRY=/home/oauth/.poetry/bin/poetry

$POETRY run python ./manage.py collectstatic --no-input
$POETRY run gunicorn wsgi
