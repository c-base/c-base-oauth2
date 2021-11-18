#!/bin/bash

POETRY=/home/oauth/.poetry/bin/poetry

export OIDC_RSA_PRIVATE_KEY="$(awk 'BEGIN{}{out=out$0"\n"}END{print out}' $OIDC_RSA_PRIVATE_KEY_FILE| sed 's/\n$//')"

$POETRY run python ./manage.py migrate
$POETRY run python ./manage.py collectstatic --no-input
$POETRY run gunicorn wsgi
