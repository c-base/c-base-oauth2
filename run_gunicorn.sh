#!/bin/bash

PYTHON=/home/oauth/c-base-oauth2/.venv/bin/python3

export OIDC_RSA_PRIVATE_KEY="$(awk 'BEGIN{}{out=out$0"\n"}END{print out}' $OIDC_RSA_PRIVATE_KEY_FILE| sed 's/\n$//')"

$PYTHON ./manage.py migrate
$PYTHON ./manage.py collectstatic --no-input
$PYTHON -m gunicorn wsgi
